#!/usr/bin/env python3
"""
Extract VideoId from various video platform URLs.

Supports: 小红书, 抖音, TikTok, B站, YouTube, 快手等
"""

import re
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    """
    Extract VideoId from video platform URL.

    Args:
        url: Video URL from supported platforms

    Returns:
        VideoId string

    Raises:
        ValueError: If URL format is not recognized
    """
    url = url.strip()

    # 小红书短链接: http://xhslink.com/o/6VbNVltFQRX
    if 'xhslink.com' in url or 'xiaohongshu.com' in url:
        match = re.search(r'/o/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)

    # 抖音: https://v.douyin.com/xxx/ or https://www.douyin.com/video/xxx
    if 'douyin.com' in url:
        # 短链接
        match = re.search(r'v\.douyin\.com/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)
        # 长链接
        match = re.search(r'/video/(\d+)', url)
        if match:
            return match.group(1)

    # TikTok: https://www.tiktok.com/@user/video/1234567890
    if 'tiktok.com' in url:
        match = re.search(r'/video/(\d+)', url)
        if match:
            return match.group(1)
        # 短链接 https://vm.tiktok.com/xxx/
        match = re.search(r'vm\.tiktok\.com/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)

    # B站: https://www.bilibili.com/video/BVxxx or https://b23.tv/xxx
    if 'bilibili.com' in url or 'b23.tv' in url:
        # BV号
        match = re.search(r'/(BV[A-Za-z0-9]+)', url)
        if match:
            return match.group(1)
        # av号
        match = re.search(r'/av(\d+)', url)
        if match:
            return f"av{match.group(1)}"
        # 短链接
        match = re.search(r'b23\.tv/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)

    # YouTube: https://www.youtube.com/watch?v=xxx or https://youtu.be/xxx
    if 'youtube.com' in url or 'youtu.be' in url:
        # youtu.be 短链接
        match = re.search(r'youtu\.be/([A-Za-z0-9_-]+)', url)
        if match:
            return match.group(1)
        # 标准链接
        parsed = urlparse(url)
        if parsed.query:
            params = parse_qs(parsed.query)
            if 'v' in params:
                return params['v'][0]

    # 快手: https://www.kuaishou.com/short-video/xxx
    if 'kuaishou.com' in url:
        match = re.search(r'/short-video/(\d+)', url)
        if match:
            return match.group(1)
        match = re.search(r'\.com/([A-Za-z0-9]+)', url)
        if match:
            return match.group(1)

    # 如果都不匹配，尝试提取 URL 最后的路径部分
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split('/') if p]
    if path_parts:
        # 返回最后一个非空路径部分
        return path_parts[-1]

    raise ValueError(f"无法从 URL 提取 VideoId: {url}")


def extract_urls(text: str) -> list[str]:
    """
    Extract video URLs from text.

    Args:
        text: Text containing video URLs

    Returns:
        List of unique video URLs
    """
    pattern = r'https?://[^\s]+(?:douyin|tiktok|youtube|youtu\.be|xiaohongshu|xhslink|bilibili|b23\.tv|kuaishou)[^\s]*'
    urls = re.findall(pattern, text)
    return list(dict.fromkeys(urls))  # 保持顺序去重


if __name__ == '__main__':
    # 测试用例
    test_urls = [
        'http://xhslink.com/o/6VbNVltFQRX',
        'http://xhslink.com/o/16X9vM9CTBo',
        'https://v.douyin.com/eFyQRjc/',
        'https://www.douyin.com/video/7123456789',
        'https://www.tiktok.com/@user/video/7123456789',
        'https://vm.tiktok.com/ZMeAbCdEf/',
        'https://www.bilibili.com/video/BV1xx411c7mD',
        'https://b23.tv/av12345678',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'https://youtu.be/dQw4w9WgXcQ',
        'https://www.kuaishou.com/short-video/1234567890',
    ]

    print("VideoId 提取测试:\n")
    for url in test_urls:
        try:
            video_id = extract_video_id(url)
            print(f"✅ {url}")
            print(f"   → {video_id}\n")
        except ValueError as e:
            print(f"❌ {url}")
            print(f"   → {e}\n")
