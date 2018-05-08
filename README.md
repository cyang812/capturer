# fork from [Litreily/capturer](https://github.com/Litreily/capturer)

# MODIFY

## LOFTER

### delete watermark
- This script will output two `.txt` file for the pic urls and raw-pic urls.

### support multi-threaded downloads
- This script will use multi-threaded to download pics after collecting all the pic's url.

### incremental update mechanism
- This script will not re-download the photos or videos if they have already been downloaded. So it will do no harm by running this script several times. In the meanwhile, you can find back the missing photos or videos.


++++++++++++++RAW+++++++++++++++++++
---

# What's Capturer

A capture tool used to capture pictures from web like Sina, LOFTER and huaban.

## How to use

- install `python` and libs
  - install `python3`
  - install `BeautifulSoup` - `bs4`
  - install `requests`
- update your [Parameters](#parameters) of each kind of web
- run `main.py` or `***_spider.py`

## Parameters

### Sina

- `uid`: user-id(10 numbers) of sina weibo that you want to capture
- `cookies`: your cookies after login the sina weibo
- `path`: directory to save the pictures

### Lofter

- `username`: username of lofter that you want to capture
- `path`: directory to save the pictures, see the function `_get_path` in `lofter_spider.py`
- `query_number`: number of blogs in each query packet, default value is 40
