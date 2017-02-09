# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:18:13 2017

@author: admin
"""

app_name = "PC_Term"
long_app = "Product Code Terminator"
version = "0_06_01A"
build_date = "02-09-2017"



dir_fresh = "Put_XMLs_Here"
dir_clean = "Processed_XMLs"
dir_dirty = "BackUp_XMLs"
dir_temp = "TEMP"
plu_xml = "PLUs.xml"
log_name = "!PC_Term Report"

email = "David@DREAM-Enterprise.com"
name = long_app + "  V" + version

value = 0
plu_count_low = 250
count_plu = 0
tag_plu = "<domain:PLU>"
var_not_found = 0
export_complete = 1
dept_tobacco_id = []
dept_alcohol_id = []
dept_food_stamps = []
full_dept_list = []



#define system varibles
wait = 3.0
width = 60
lines = 35
cent_width = int(width)-1
