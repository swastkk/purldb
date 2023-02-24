# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# purldb is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/purldb for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import json
import os

import attr
import mock

from minecode.management import scanning
from minecode.utils_test import JsonBasedTesting


class ScanCodeIOAPIHelperFunctionTest(JsonBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'testfiles')

    @mock.patch('requests.get')
    def testscanning_query_scans(self, mock_get):
        mock_get.return_value = mock.Mock(ok=True)
        scan_info_response_loc = self.get_test_loc('scancodeio/scan_request_lookup.json')
        with open(scan_info_response_loc, 'rb') as f:
            mock_get.return_value.json.return_value = json.loads(f.read())

        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        uri = 'http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar'
        result = scanning.query_scans(uri=uri, api_url=api_url, api_auth=api_auth)

        expected = scanning.Scan(
            url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/',
            uuid='177eb27a-25d2-4ef0-b608-5a84ea9b1ef1',
            uri='http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar',
            sha1=None,
            md5=None,
            size=None,
            created_date='2018-10-22T19:45:51.667927Z',
            task_start_date=None,
            task_end_date=None,
            task_exitcode=None,
            status='not started yet',
            execution_time=None,
            data_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/data/',
            summary_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/summary/'
        )

        expected = attr.asdict(expected)
        self.assertEqual(expected, result)

    @mock.patch('requests.post')
    def testscanning_submit_scan(self, mock_post):
        test_loc = self.get_test_loc('scancodeio/scan_request_response.json')
        mock_post.return_value = mock.Mock(ok=True)
        with open(test_loc, 'rb') as f:
            mock_post.return_value.json.return_value = json.loads(f.read())
        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        uri = 'http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar'
        result = scanning.submit_scan(uri=uri, api_url=api_url, api_auth=api_auth)
        expected = scanning.Scan(
            url='http://127.0.0.1:8001/api/scans/5463cc42-abe8-4ac7-9eda-58b03ec7e881/',
            uuid='5463cc42-abe8-4ac7-9eda-58b03ec7e881',
            uri='http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar',
            sha1=None,
            md5=None,
            size=None,
            created_date='2019-02-04T23:06:46.343135Z',
            task_start_date=None,
            task_end_date=None,
            task_exitcode=None,
            status='not started yet',
            execution_time=None,
            data_url='http://127.0.0.1:8001/api/scans/5463cc42-abe8-4ac7-9eda-58b03ec7e881/data/',
            summary_url='http://127.0.0.1:8001/api/scans/5463cc42-abe8-4ac7-9eda-58b03ec7e881/summary/'
        )
        expected = attr.asdict(expected)
        result = attr.asdict(result)
        self.assertEqual(expected, result)

    @mock.patch('requests.post')
    @mock.patch('requests.get')
    def testscanning_submit_scan_uri_exists(self, mock_post, mock_get):
        self.maxDiff = None
        mock_post.return_value = mock.Mock(ok=False)
        scan_request_response_loc = self.get_test_loc('scancodeio/scan_exists_for_uri.json')
        with open(scan_request_response_loc, 'rb') as f:
            mock_post.return_value.json.return_value = json.loads(f.read())

        mock_get.return_value = mock.Mock(ok=True)
        scan_info_response_loc = self.get_test_loc('scancodeio/new_scan_request.json')
        with open(scan_info_response_loc, 'rb') as f:
            mock_get.return_value.json.return_value = json.loads(f.read())

        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        uri = 'http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar'
        result = scanning.submit_scan(uri=uri, api_url=api_url, api_auth=api_auth)

        expected = scanning.Scan(
            url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/',
            uuid='177eb27a-25d2-4ef0-b608-5a84ea9b1ef1',
            uri='http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar',
            sha1=None,
            md5=None,
            size=None,
            created_date='2018-10-22T19:45:51.667927Z',
            task_start_date=None,
            task_end_date=None,
            task_exitcode=None,
            status='not started yet',
            execution_time=None,
            data_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/data/',
            summary_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/summary/'
        )

        expected = attr.asdict(expected)
        result = attr.asdict(result)
        self.assertEqual(expected, result)

    def testscanning_get_scan_url(self):
        scan_uuid = '177eb27a-25d2-4ef0-b608-5a84ea9b1ef1'
        api_url_scans = 'http://127.0.0.1:8001/api/scans/'
        suffix = 'data'
        result = scanning.get_scan_url(scan_uuid=scan_uuid, api_url=api_url_scans)
        expected = 'http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/'
        self.assertEqual(expected, result)
        result_with_suffix = scanning.get_scan_url(scan_uuid=scan_uuid, api_url=api_url_scans, suffix=suffix)
        expected_with_suffix = 'http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/data/'
        self.assertEqual(expected_with_suffix, result_with_suffix)

    @mock.patch('requests.get')
    def testscanning_get_scan_info(self, mock_get):
        test_loc = self.get_test_loc('scancodeio/get_scan_info.json')
        mock_get.return_value = mock.Mock(ok=True)
        with open(test_loc, 'rb') as f:
            mock_get.return_value.json.return_value = json.loads(f.read())
        scan_uuid = '177eb27a-25d2-4ef0-b608-5a84ea9b1ef1'
        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        result = scanning.get_scan_info(scan_uuid=scan_uuid, api_url=api_url, api_auth=api_auth)
        expected = scanning.Scan(
            url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/',
            uuid='177eb27a-25d2-4ef0-b608-5a84ea9b1ef1',
            uri='http://repo1.maven.org/maven2/maven/wagon-api/20040705.181715/wagon-api-20040705.181715.jar',
            sha1='feff0d7bacd11d37a9c96daed87dc1db163065b1',
            md5='57431f2f6d5841eebdb964b04091b8ed',
            size=47069,
            created_date='2018-10-22T19:45:51.667927Z',
            task_start_date='2018-10-22T19:45:51.689498Z',
            task_end_date='2018-10-22T19:45:59.980194Z',
            task_exitcode=0,
            status='completed',
            execution_time=8.290696,
            data_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/data/',
            summary_url='http://127.0.0.1:8001/api/scans/177eb27a-25d2-4ef0-b608-5a84ea9b1ef1/summary/'
        )
        expected = attr.asdict(expected)
        result = attr.asdict(result)
        self.assertEqual(expected, result)

    @mock.patch('requests.get')
    def testscanning_get_scan_summary(self, mock_get):
        test_loc = self.get_test_loc('scancodeio/get_scan_summary.json')
        mock_get.return_value = mock.Mock(ok=True)
        with open(test_loc, 'rb') as f:
            mock_get.return_value.json.return_value = json.loads(f.read())
        scan_uuid = '177eb27a-25d2-4ef0-b608-5a84ea9b1ef1'
        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        result = scanning.get_scan_summary(scan_uuid=scan_uuid, api_url=api_url, api_auth=api_auth)
        expected = {
            'license_expressions': [
                {
                    'value': None,
                    'count': 45
                }
            ],
            'copyrights': [
                {
                    'value': None,
                    'count': 45
                }
            ],
            'holders': [
                {
                    'value': None,
                    'count': 45
                }
            ],
            'authors': [
                {
                    'value': None,
                    'count': 45
                }
            ],
            'programming_language': [
                {
                    'value': None,
                    'count': 45
                }
            ]
        }
        self.assertEqual(expected, result)

    @mock.patch('requests.get')
    def testscanning_get_scan_data(self, mock_get):
        test_loc = self.get_test_loc('scancodeio/get_scan_data.json')
        mock_get.return_value = mock.Mock(ok=True)
        with open(test_loc, 'rb') as f:
            mock_get.return_value.json.return_value = json.loads(f.read())
        scan_uuid = '177eb27a-25d2-4ef0-b608-5a84ea9b1ef1'
        api_url = 'http://127.0.0.1:8001/api/'
        api_auth = ('', '')
        expected_loc = self.get_test_loc('scancodeio/get_scan_data_expected.json')
        result = scanning.get_scan_summary(scan_uuid=scan_uuid, api_url=api_url, api_auth=api_auth)
        with open(expected_loc, 'rb') as f:
            expected = json.loads(f.read())
        self.assertEqual(expected['files'], result['files'])