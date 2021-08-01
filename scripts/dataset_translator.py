from translate import Translator
import json


def translate_dataset(file_loc, output_file):
    # parse file
    with open(file_loc, 'r') as json_file:
        dataset_str = json_file.read()
    dataset_obj = json.loads(dataset_str)

    # translate here

    # write output file
    with open(output_file, 'w') as outfile:
        json.dump(dataset_obj, outfile)


def main():
    # init translator
    translator = Translator(to_lang="pt")

    # define train files locations
    train_dataset_loc = "../data/squad_en/train-v2.0.json"
    train_output_file = "../data/squad_pt/train-v2.0.json"

    # define dev files locations
    dev_dataset_loc = "../data/squad_en/dev-v2.0.json"
    dev_output_file = "../data/squad_pt/dev-v2.0.json"

    # translate train dataset
    translate_dataset(train_dataset_loc, train_output_file)

    # translate dev dataset
    translate_dataset(dev_dataset_loc, dev_output_file)


if __name__ == "__main__":
    main()
