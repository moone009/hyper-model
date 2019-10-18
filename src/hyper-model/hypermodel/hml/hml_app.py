
import click
from typing import Dict
from kfp import dsl
from hypermodel.hml.hml_pipeline_app import HmlPipelineApp
from hypermodel.hml.hml_inference_app import HmlInferenceApp

from hypermodel.platform.gcp.services import GooglePlatformServices


# This is the default `click` entrypoint for kicking off the command line


class HmlApp():
    def __init__(self, name, platform, config):
        self.name = name
        self.platform = platform
        self.services = self.get_services(platform)

    
        self.pipelines = HmlPipelineApp(name, self.services, self.cli_root, config)
        self.inference = HmlInferenceApp(name, self.services, self.cli_root, config)

    @click.group()
    @click.pass_context
    def cli_root(ctx):
        return


    def get_services(self, platform):
        if platform == "GCP":
            return GooglePlatformServices()

    def start(self):
        context = {
            "app": self,
            "services": self.services
        }

        self.cli_root(obj=context, auto_envvar_prefix="HML")

