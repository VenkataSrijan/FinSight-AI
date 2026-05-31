from app.services.ml.dataset_service import (
    DatasetService,
)


def test_dataset_service_creation():

    service = DatasetService()

    assert service is not None