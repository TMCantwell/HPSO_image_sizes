""" This program calculates the total image storage for a HPSO. Values used are
taken from Table 8 and Table 9 in SKA-TEL-SDP-0000038 revision 02 """

import matplotlib.pyplot as plt
import numpy as np


class HPSO:
    """ This class defines a HPSO"""

    def __init__(self, name, size_single_image, total_time, number_fields,
                 time_res_of_image, fraction_of_time):
        """ Return a HPSO whose name is *name*. size_single_image should be in
        bytes. Times are in hours"""
        self.name = name
        self.size_single_image = size_single_image
        self.total_time = total_time
        self.number_fields = number_fields
        self.time_per_image = time_res_of_image
        self.time_per_field = self.total_time/self.number_fields
        self.total_number_images = (self.time_per_field/self.time_per_image) \
            * self.number_fields
        self.number_years_running = int(np.ceil(self.total_time
                                        / (fraction_of_time*365*24)))

    def calc_storage(self):
        """ Calculates the total storage for HPSO in Pbytes"""
        self.total_storage = self.total_number_images*self.size_single_image \
            / 1e15
        print("The storage for HPSO "+self.name+" is :\t"
              + str(self.total_storage))
        self.data_per_year = self.total_storage*4/self.number_years_running
        self.timeline = np.zeros(16)
        self.timeline[1:self.number_years_running+1] = self.data_per_year
        self.timeline = self.timeline * np.arange(16)
        self.timeline[self.number_years_running+1:] = max(self.timeline)

    def plot_timeline(self, ax, c, style):
        """ Plots data storage requirements (including advanced data products)
            as a function of time."""
        ax.plot(np.linspace(0, 15, 16), self.timeline, color=c,
                linestyle=style, label=self.name)


class HPSONIP:
    """ This class defines an NIP HPSO"""

    def __init__(self, name, bits_per_sec, total_time, fraction_of_time):
        self.name = name
        self.time = total_time
        self.bits_per_sec = bits_per_sec
        self.number_years_running = int(np.ceil(self.time
                                        / (fraction_of_time*365*24)))

    def calc_storage(self):
        self.total_storage = self.time*3600*self.bits_per_sec*0.125/1e15
        print("The storage for HPSO "+self.name+" is :\t"
              + str(self.total_storage))
        self.data_per_year = self.total_storage*4/self.number_years_running
        self.timeline = np.zeros(16)
        self.timeline[1:self.number_years_running+1] = self.data_per_year
        self.timeline = self.timeline * np.arange(16)
        self.timeline[self.number_years_running+1:] = max(self.timeline)

    def plot_timeline(self, ax, c, style):
        """ Plots data storage requirements (including advanced data products)
            as a function of time."""
        ax.plot(np.linspace(0, 15, 16), self.timeline, color=c,
                linestyle=style, label=self.name)


eor_1 = HPSO(name='EoR:1', size_single_image=14e12,  total_time=5000,
             number_fields=5, time_res_of_image=6, fraction_of_time=0.16)
eor_2a = HPSO(name='EoR:2a', size_single_image=14e12,  total_time=5000,
              number_fields=50, time_res_of_image=6, fraction_of_time=0.16)
eor_2b = HPSO(name='EoR:2b', size_single_image=14e12,  total_time=5000,
              number_fields=500, time_res_of_image=6, fraction_of_time=0.16)
HI_13 = HPSO(name='HI:13', size_single_image=16.1e12,  total_time=5000,
             number_fields=5, time_res_of_image=6, fraction_of_time=0.07)
HI_14 = HPSO(name='HI:14', size_single_image=8.3e12,  total_time=2000,
             number_fields=10, time_res_of_image=6, fraction_of_time=0.03)
HI_15 = HPSO(name='HI:15', size_single_image=1.6e12,  total_time=12600,
             number_fields=2842, time_res_of_image=4.4, fraction_of_time=0.19)
col_22 = HPSO(name='Cradle of Life:22', size_single_image=48.8e12,
              total_time=6000, number_fields=10, time_res_of_image=6,
              fraction_of_time=0.09)
magnetism_27 = HPSO(name='Magnetism:27', size_single_image=1.5e12,
                    total_time=10000, number_fields=8157,
                    time_res_of_image=0.1, fraction_of_time=0.15)
continuum_37a = HPSO(name='Continuum:37a', size_single_image=34.7e12,
                     total_time=2000, number_fields=21, time_res_of_image=6,
                     fraction_of_time=0.03)
continuum_37b = HPSO(name='Continuum:37b', size_single_image=34.7e12,
                     total_time=2000, number_fields=1, time_res_of_image=6,
                     fraction_of_time=0.03)
continuum_37c = HPSO(name='Continuum:37c', size_single_image=5.9e12,
                     total_time=10000, number_fields=2632, time_res_of_image=6,
                     fraction_of_time=0.15)
continuum_38a = HPSO(name='Continuum:38a', size_single_image=110.7e12,
                     total_time=1000, number_fields=61, time_res_of_image=6,
                     fraction_of_time=0.01)
continuum_38b = HPSO(name='Continuum:38a', size_single_image=112.5e12,
                     total_time=1000, number_fields=1, time_res_of_image=6,
                     fraction_of_time=0.01)
cosmology_storage = magnetism_27.size_single_image \
    * (magnetism_27.time_per_field/magnetism_27.time_per_image)*9
pulsars_4 = HPSONIP(name='Pulsars:4', bits_per_sec=0.7e9,
                    total_time=(12750+800+2400), fraction_of_time=0.45)
pulsars_5 = HPSONIP(name='Pulsars:5', bits_per_sec=0.6e9,
                    total_time=(4300+1600+1600), fraction_of_time=0.17)
transients_18 = HPSONIP(name='Transients:18', bits_per_sec=0.1e9,
                        total_time=10000, fraction_of_time=0.15)

eor_1.calc_storage()
eor_2a.calc_storage()
eor_2b.calc_storage()
pulsars_4.calc_storage()
pulsars_5.calc_storage()
HI_13.calc_storage()
HI_14.calc_storage()
HI_15.calc_storage()
transients_18.calc_storage()
col_22.calc_storage()
magnetism_27.calc_storage()
print("The storage for HPSO Cosmology:33 is :\t"+str(cosmology_storage/1e15))
continuum_37a.calc_storage()
continuum_37b.calc_storage()
continuum_37c.calc_storage()
continuum_38a.calc_storage()
continuum_38b.calc_storage()
# print(str(Magnetism_27.time_per_field*9))

ax1 = plt.subplot(111)
HI_13.plot_timeline(ax1, 'gold', '-')
HI_14.plot_timeline(ax1, 'gold', '--')
HI_15.plot_timeline(ax1, 'gold', '-.')
continuum_37a.plot_timeline(ax1, 'blue', '-')
continuum_37b.plot_timeline(ax1, 'blue', '--')
continuum_37c.plot_timeline(ax1, 'blue', '-.')
continuum_38a.plot_timeline(ax1, 'green', '-')
continuum_38b.plot_timeline(ax1, 'green', '--')
ax1.set_xlim(0, 15)
ax1.set_xlabel('year')
ax1.set_ylabel('storage requirments (PB)')
ax1.legend()
plt.savefig('timeline1.pdf')
plt.show()

ax1 = plt.subplot(111)
# eor_1.plot_timeline(ax1, 'black', '-')
# eor_2a.plot_timeline(ax1, 'black', '--')
# eor_2b.plot_timeline(ax1, 'black', '-.')
eor_data_per_year = ((28.3*3)+(116*3)+(359.1))/15
ax1.plot(np.linspace(0, 15, 16), np.linspace(0, eor_data_per_year*15, 16),
         color='black', label='EoR')
col_22.plot_timeline(ax1, 'red', '-')
magnetism_27.plot_timeline(ax1, 'purple', '-')
ax1.set_xlim(0, 15)
ax1.set_xlabel('year')
ax1.set_ylabel('storage requirments (PB)')
ax1.legend()
plt.savefig('timeline2.pdf')
plt.show()

ax1 = plt.subplot(111)
pulsars_4.plot_timeline(ax1, 'green', '-')
pulsars_5.plot_timeline(ax1, 'green', '--')
transients_18.plot_timeline(ax1, 'orange', '-')
ax1.set_xlim(0, 15)
ax1.set_xlabel('year')
ax1.set_ylabel('storage requirments (PB)')
ax1.legend()
plt.savefig('timeline3.pdf')
plt.show()

eor = np.zeros(16)
eor[1:] = ((28.3*3*4)+(11.6*3*4))/15
eor = eor * np.arange(16)
total_timeline = eor+col_22.timeline \
                      + magnetism_27.timeline+pulsars_4.timeline \
                      + pulsars_5.timeline+transients_18.timeline \
                      + HI_13.timeline+HI_14.timeline \
                      + HI_15.timeline+continuum_37a.timeline \
                      + continuum_37b.timeline \
                      + continuum_37c.timeline \
                      + continuum_38a.timeline \
                      + continuum_38b.timeline
ax1 = plt.subplot(111)
ax1.plot(np.linspace(0, 15, 16), total_timeline, color='black',
         linestyle='-', label='Total Storage')
ax1.set_xlim(0, 15)
ax1.set_xlabel('year')
ax1.set_ylabel('storage requirments (PB)')
ax1.legend()
plt.savefig('timeline4.pdf')
plt.show()
