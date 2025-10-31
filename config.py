"""config.py"""
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor<br>
        -----------<br>

        Variables denoting a path - including or excluding a filename - have an underscore suffix; this suffix is
        excluded for names such as warehouse, storage, depository, etc.<br><br>
        """

        '''
        Keys
        '''
        self.architecture = 'arc-state-space-mixture'
        self.s3_parameters_key = 's3_parameters.yaml'
        self.argument_key = f'artefacts/architecture/{self.architecture}/arguments.json'
        self.metadata_ = 'arc-state-space-mixture-metrics/external'

        '''
        Project Metadata
        '''
        self.project_tag = 'hydrography'
        self.project_key_name = 'HydrographyProject'

        '''
        Local Paths
        '''
        self.data_ = os.path.join(os.getcwd(), 'data')
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        self.pathway_ = os.path.join(self.warehouse, self.architecture)
        self.points_ = os.path.join(self.pathway_, 'points')
        self.menu_ = os.path.join(self.pathway_, 'menu')

        '''
        Cloud Prefix: Destination
        '''
        self.prefix = f'warehouse/{self.architecture}'

        '''
        Cloud Prefix: Source
        '''
        self.origin_ = f'assets/{self.architecture}'
