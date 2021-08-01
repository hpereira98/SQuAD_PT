from googletrans import Translator
import json


def translate_dataset(translator, file_loc, output_file):
    # parse file
    with open(file_loc, 'r') as json_file:
        dataset_str = json_file.read()
    dataset_obj = json.loads(dataset_str)

    # translate here
    questions = dataset_obj['data']
    for i, question in enumerate(questions):
        paragraphs = question['paragraphs']
        for j, paragraph in enumerate(paragraphs):
            qas = paragraph['qas']
            for k, qa in enumerate(qas):
                if 'question' in qa:
                    translated_question = translator.translate(
                        qa['question'], src='en', dest='pt').text
                    qa['question'] = translated_question

                if 'answers' in qa:
                    answers = qa['answers']
                    for o, answer in enumerate(answers):
                        translated_answer = translator.translate(
                            answer['text'], src='en', dest='pt').text
                        answers[o] = translated_answer
                    qa['answers'] = answers

                if 'plausible_answers' in qa:
                    plausible_answers = qa['plausible_answers']
                    for p, answer in enumerate(plausible_answers):
                        translated_answer = translator.translate(
                            answer['text'], src='en', dest='pt').text
                        plausible_answers[p] = translated_answer
                    qa['plausible_answers'] = plausible_answers
                qas[k] = qa

            paragraph['qas'] = qas
            translated_context = translator.translate(
                paragraph['context'], src='en', dest='pt').text
            paragraph['context'] = translated_context
            paragraphs[j] = paragraph

        question['paragraphs'] = paragraphs
        questions[i] = question

    dataset_obj['data'] = questions

    # write output file
    with open(output_file, 'w') as outfile:
        json.dump(dataset_obj, outfile)


def main():
    # init translator
    translator = Translator()

    # define train files locations
    train_dataset_loc = "../data/squad_en/train-v2.0.json"
    train_output_file = "../data/squad_pt/train-v2.0.json"

    # define dev files locations
    dev_dataset_loc = "../data/squad_en/dev-v2.0.json"
    dev_output_file = "../data/squad_pt/dev-v2.0.json"

    # translate train dataset
    print("Translating Train Dataset...")
    translate_dataset(translator, train_dataset_loc, train_output_file)

    # translate dev dataset
    print("Translating Dev Dataset...")
    translate_dataset(translator, dev_dataset_loc, dev_output_file)


if __name__ == "__main__":
    main()
