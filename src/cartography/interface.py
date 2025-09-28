"""Module cartography/interface.py"""
import logging

import boto3

import src.cartography.risks
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.keys
import src.cartography.maps


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

        self.__maps = src.cartography.maps.Maps(connector=self.__connector, s3_parameters=self.__s3_parameters)

    def exc(self):
        """

        :return:
        """

        coarse = self.__maps.exc(key_name='cartography/coarse.geojson')
        coarse.info()
        logging.info(coarse)
        care = self.__maps.exc(key_name='cartography/care_and_coarse_catchments.geojson')
        care['latitude'] = care.geometry.apply(lambda k: k.y)
        care['longitude'] = care.geometry.apply(lambda k: k.x)
        care.info()
        logging.info(care)

        # The list of rate files
        elements = src.s3.keys.Keys(service=self.__service, bucket_name=self.__s3_parameters.external).excerpt(
            prefix='warehouse/risks/points/', delimiter='')
        logging.info(elements)

        # Per rate risk file
        for key_name in elements:
            risks = src.cartography.risks.Risks(
                s3_parameters=self.__s3_parameters, connector=self.__connector, key_name=key_name).exc()
            risks.info()
            logging.info(risks)
