#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'sortedcontainers>=1.5.9',
    'requests>=2.13.0',
    'six>=1.10.0',
    'websocket-client>=0.40.0'
]

setup(
    name='bitstamp_wsclient',
    version='1.0.0',
    author='Aitor Sanchez',
    author_email='aitorsanchezmansilla@gmail.com',
    license='MIT',
    url='https://github.com/aitorSTL/bitstamp_ws_client',
    packages=find_packages(),
    install_requires=install_requires,    
    description='The unofficial Python websocket client for the Bitstamp API',
    download_url='https://github.com/aitorSTL/bitstamp_ws_client/archive/main.zip',
    keywords=['bitstamp', 'bitstamp-api', 'orderbook', 'trade', 'bitcoin', 'ethereum', 'BTC', 'ETH', 'client', 'api', 'wrapper',
              'exchange', 'crypto', 'currency', 'trading', 'trading-api', 'coinbase', 'pro', 'prime', 'websocket'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
