"""Module risks/interface.py"""
import json
import logging
import io

import boto3
import pandas as pd

import src.elements.s3_parameters as s3p
import src.s3.unload


class Interface:
    """
    An interface to the risks programs
    """

    def __init__(self,s3_parameters: s3p.S3Parameters, connector: boto3.session.Session, ):
        """

        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.<br>
        :param connector: An instance of boto3.session.Session
        """

        self.__s3_parameters = s3_parameters

        # An instance for S3 interactions
        self.__s3_client: boto3.session.Session.client = connector.client(
            service_name='s3')

        self.__unload = src.s3.unload.Unload(s3_client=self.__s3_client)

    def exc(self):
        """

        :return:
        """

        # Try
        key_name = 'warehouse/risks/points/0004.json'
        buffer = self.__unload.exc(bucket_name=self.__s3_parameters.external, key_name=key_name)

        try:
            data = json.loads(buffer)
        except json.JSONDecodeError as err:
            raise err from err
        logging.info(data)

        for j in range(len(data)):

            node:dict = data[j]
            node.pop('catchment_id', None)
            node.pop('catchment_name', None)
            logging.info(node)

            frame = pd.DataFrame.from_records(data=node['data'], index=node['index'], columns=node['columns'])
            logging.info(frame)
