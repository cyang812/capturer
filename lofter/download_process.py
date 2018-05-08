# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import urllib.request
import requests
from multiprocessing import Process, Queue, Pool

url_filename = 'url_list.txt'

# PROXIES = { "http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080" } 
PROXIES = {}

def delete_watermark(url_lists):
	rst = []

	for url_list in url_lists:
		try:
			url_list = url_list.split('?imageView')[0]
			# print(url_list)
			rst.append(url_list)
		except Exception as e:
			print(e)

	return rst		

def save_list_to_file(l_name, f_name):
    l_name = sorted(set(l_name), key = l_name.index)     
    # print('l_name = ', l_name)     
    print('l_name len = ', len(l_name))

    with open(f_name, 'w', encoding='utf-8') as file:
        for x in range(0,len(l_name)):
            file.write(str(l_name[x])+'\n')

def get_url():
	with open(url_filename, "r") as f:
	    raw_sites = f.read()

	raw_sites = raw_sites.replace("\n", ",") 
	raw_sites = raw_sites.split(",")

	sites = list()
	for raw_site in raw_sites:
	    site = raw_site.lstrip().rstrip()
	    if site:
	        sites.append(site)

	print('list_len = ',len(sites))	        
	return sites

def get_filename(url):
	name = url.split("/")[-1].split("?")[0]
	return name    

def download_one(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
	name = get_filename(url)

	file_path = os.path.join(name)
	if not os.path.isfile(file_path):
		try:
			r = requests.get(url,proxies=PROXIES,headers = headers)
			print('downloading ->',name)

			with open(name, "wb") as code:
		   		code.write(r.content)
		except Exception as e:
			print('downloading err ->', name)
			pass
	else:
		print("file exist")		   

def chdir(path):

	current_folder = os.getcwd()
	print(current_folder)
	target_folder = os.path.join(current_folder, path)
	if not os.path.isdir(target_folder):
		os.mkdir(target_folder)
	os.chdir(target_folder)

def download(imgs, processes=10):
    """ 并发下载所有图片 """
    start_time = time.time()
    pool = Pool(processes)
    for img in imgs:
        pool.apply_async(download_one, (img, ))

    pool.close()
    pool.join()
    end_time = time.time()
    print('下载完毕,用时:%s秒,总数%d' % (end_time - start_time, len(imgs)))

# module test
if __name__ == '__main__':
	url = get_url()
	
	# url = delete_watermark(url)
	# save_list_to_file(url, 'new_url_list.txt')

	chdir('cy950812')
	download(url)

