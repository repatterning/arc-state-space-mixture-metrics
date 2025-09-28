"""Module cartography/data.py"""
import geopandas
import pandas as pd


class Data:
    """
    Data
    """

    def __init__(self, care: geopandas.GeoDataFrame):
        """

        :param care: Care home frame
        """

        self.__care = self.__get_care(care=care.copy())

        # fields
        self.__f_care = ['catchment_id', 'catchment_name', 'focus', 'latitude', 'longitude', 'organisation',
                         'town', 'local_authority']
        self.__f_risks = ['catchment_id', 'catchment_name', 'focus', 'latitude', 'longitude', 'station_name',
                          'latest', 'maximum', 'minimum', 'median', 'ending', 'river_name']

    @staticmethod
    def __get_care(care: geopandas.GeoDataFrame):
        """

        :param care: Care home frame
        :return:
        """

        care['latitude'] = care.geometry.apply(lambda k: k.y)
        care['longitude'] = care.geometry.apply(lambda k: k.x)
        care['focus'] = 'elders'

        return care

    def exc(self, risks: pd.DataFrame):
        """

        :param risks: A frame of river level change rates, etc.
        :return:
        """

        risks['focus'] = 'gauge'

        # Concatenating
        data = pd.concat([self.__care[self.__f_care], risks[self.__f_risks]], axis=0, ignore_index=True)

        return data
