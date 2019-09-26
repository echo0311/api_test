# -*- coding: utf-8 -*-
from abc import abstractmethod

from base.api_requests import RunMethod
from util.operation_ini import OperationIni
from util.operation_header import OperationHeader
from util.operation_json import OperationJson


class BaseAPI(object):
    def __init__(self):
        self.oper_ini = OperationIni()
        self.oper_h = OperationHeader()
        self.run_method = RunMethod()
        self.oper_json = OperationJson()
        # self.path = path

    def get_host(self):
        host = self.oper_ini.get_value('host', 'url')
        return host

    @abstractmethod
    def get_path(self):
        pass

    def get_url(self):
        url = self.get_host() + self.get_path()
        return url

    @abstractmethod
    def get_header(self):
        pass

    def get_request_data(self):
        pass

    def run(self):
        pass
