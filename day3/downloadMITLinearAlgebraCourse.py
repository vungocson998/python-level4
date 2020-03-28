# Download images from unsplash
# Use requests lib to get that content
import requests
import time
import concurrent.futures

vid_urls = [
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/11.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/12.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/13.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/14.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/15.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/16.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/17.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/18.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/19.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/20.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/21.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/22.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/23.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/24.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/24b.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/25.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/26.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/27.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/28.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/29.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/30.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/31.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/32.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/33.mp4',
    'https://ia902205.us.archive.org/18/items/MIT18.06S05_MP4/34.mp4'
]

t1 = time.perf_counter()


def download_video(vid_url):
    # Download image data
    vid_bytes = requests.get(vid_url).content
    # Create the name
    vid_name = vid_url.split('/')[6]
    vid_name = f'/home/ted/Documents/hust/LinearAlgebra/{vid_name}'
    # Save image in file
    with open(vid_name, 'wb') as vid_file:
        vid_file.write(vid_bytes)
        print(f'{vid_name} was downloaded...')

# Using threading pool executor to download all of the images:
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(download_video, vid_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')