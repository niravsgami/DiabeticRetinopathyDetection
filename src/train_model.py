from configuration import data_params, data_transforms, training_params, model_params, optimizer_params
from data_loading import get_train_valid_loader, get_test_loader
from output_writing import write_submission_csv
from trainer import ModelTrainer

if __name__ == '__main__':

    train_dataset_loader, valid_dataset_loader = get_train_valid_loader(data_params['train_path'],
                                                                        data_params['label_path'],
                                                                        random_seed=54321,
                                                                        batch_size=data_params['batch_size'],
                                                                        train_transforms=data_transforms,
                                                                        valid_transforms=data_transforms)
    test_dataset_loader = get_test_loader(data_params['test_path'],
                                          batch_size=data_params['batch_size'],
                                          transforms=data_transforms)

    model = model_params['model'](**model_params['model_kwargs'])

    model_trainer = ModelTrainer(model, train_dataset_loader, valid_dataset_loader, test_dataset_loader,
                                 optimizer_args=optimizer_params)
    model_trainer.train_model(**training_params)

    predictions, image_names = model_trainer.predict_on_test()

    write_submission_csv(predictions, image_names, data_params['submission_file'])


