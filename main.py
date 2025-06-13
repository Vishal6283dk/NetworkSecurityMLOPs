from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.entity.config_entity import (DataIngestionConfig,
                                                  DataValidationConfig,
                                                  DataTransformationConfig)


import sys


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()

        data_ingestion_config=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config)

        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")

        print(data_ingestion_artifact)




        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact,data_validation_config)

        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        
        print(data_validation_artifact)
        



        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)

        logging.info("Initiate the data Transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data Transformation completed")

        print(data_transformation_artifact)
        
        

    except Exception as e:
            raise NetworkSecurityException(e,sys)