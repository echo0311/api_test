# -*- coding: utf-8 -*-

vdc_id ='5'
path = '/api/cloud/virtualdatacenters/%s/virtualappliances?startwith=0&limit=30'%int(vdc_id)
print(path)