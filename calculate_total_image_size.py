""" This program calculates the total image storage for a HPSO. Values used are
taken from Table 8 and Table 9 in SKA-TEL-SDP-0000038 revision 02 """


class HPSO:
    """ This class defines a HPSO"""

    def __init__(self, name, size_single_image, total_time, number_fields,
                 time_res_of_image):
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

    def calc_storage(self):
        """ Calculates the total storage for HPSO in Pbytes"""
        self.total_storage = self.total_number_images*self.size_single_image \
            / 1e15
        print("The storage for HPSO "+self.name+" is :\t"
              + str(self.total_storage))


eor_1 = HPSO(name='EoR:1', size_single_image=14e12,  total_time=5000,
             number_fields=5, time_res_of_image=6)
eor_2a = HPSO(name='EoR:2a', size_single_image=14e12,  total_time=5000,
              number_fields=50, time_res_of_image=6)
eor_2b = HPSO(name='EoR:2b', size_single_image=14e12,  total_time=5000,
              number_fields=500, time_res_of_image=6)
HI_13 = HPSO(name='HI:13', size_single_image=16.1e12,  total_time=5000,
             number_fields=5, time_res_of_image=6)
HI_14 = HPSO(name='HI:14', size_single_image=8.3e12,  total_time=2000,
             number_fields=10, time_res_of_image=6)
HI_15 = HPSO(name='HI:15', size_single_image=1.6e12,  total_time=12600,
             number_fields=2842, time_res_of_image=4.4)
col_22 = HPSO(name='Cradle of Life:22', size_single_image=48.8e12,
              total_time=6000, number_fields=10, time_res_of_image=6)
Magnetism_27 = HPSO(name='Magnetism:27', size_single_image=1.5e12,
                    total_time=10000, number_fields=8157,
                    time_res_of_image=0.1)
Continuum_37a = HPSO(name='Continuum:37a', size_single_image=34.7e12,
                     total_time=2000, number_fields=21, time_res_of_image=6)
Continuum_37b = HPSO(name='Continuum:37b', size_single_image=34.7e12,
                     total_time=2000, number_fields=1, time_res_of_image=6)
Continuum_37c = HPSO(name='Continuum:37c', size_single_image=5.9e12,
                     total_time=10000, number_fields=2632, time_res_of_image=6)
Continuum_38a = HPSO(name='Continuum:38a', size_single_image=110.7e12,
                     total_time=1000, number_fields=61, time_res_of_image=6)
Continuum_38b = HPSO(name='Continuum:38a', size_single_image=112.5e12,
                     total_time=1000, number_fields=1, time_res_of_image=6)

eor_1.calc_storage()
eor_2a.calc_storage()
eor_2b.calc_storage()
HI_13.calc_storage()
HI_14.calc_storage()
HI_15.calc_storage()
col_22.calc_storage()
Magnetism_27.calc_storage()
Continuum_37a.calc_storage()
Continuum_37b.calc_storage()
Continuum_37c.calc_storage()
Continuum_38a.calc_storage()
Continuum_38b.calc_storage()
