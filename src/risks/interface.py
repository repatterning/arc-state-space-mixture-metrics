"""Module risks/interface.py"""
import logging

import boto3

import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.risks.data
import src.s3.keys
import src.s3.unload


class Interface:
    """
    An interface to the risks programs
    """

    def __init__(self, connector: boto3.session.Session, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param connector: An instance of boto3.session.Session
        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.<br>
        """

        self.__connector = connector
        self.__service = service
        self.__s3_parameters = s3_parameters

    def exc(self):
        """

        :return:
        """

        elements = src.s3.keys.Keys(service=self.__service, bucket_name=self.__s3_parameters.external).excerpt(
            prefix='warehouse/risks/points/', delimiter='')
        logging.info(elements)

        for key_name in elements:
            instances = src.risks.data.Data(
                s3_parameters=self.__s3_parameters, connector=self.__connector, key_name=key_name).exc()
            logging.info(instances)
