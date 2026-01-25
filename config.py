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
        self.argument_key = f'architectures/{self.architecture}/arguments.json'
        self.metadata_ = f'architectures/{self.architecture}/metrics/external'

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

        sections = ['architecture', self.architecture, 'live']
        self.pathway_ = os.path.join(self.warehouse, *sections)
        self.points_ = os.path.join(self.pathway_, 'points')
        self.menu_ = os.path.join(self.pathway_, 'menu')

        '''
        Cloud Prefix: Destination
        '''
        self.prefix = 'warehouse/' + '/'.join(sections)

        '''
        Cloud Prefix: Source of artefacts
        '''
        self.artefacts_ = f'architecture/{self.architecture}/live'
