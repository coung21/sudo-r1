import os
import argparse
import json
from datasets import load_dataset
from pprint import pprint
import jinja2
from prompt import ONE_SHOT_STANDARD_PROMPT, ONE_SHOT_VARIANT_PROMPT
from utils import pretty_print_visual_elements, format_sudoku_board


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_dir", type=str, default="./data/sudoku")
    args = parser.parse_args()

    # Load the dataset
    train_dataset = load_dataset("SakanaAI/Sudoku-Bench", "ctc")['test']
    test_dataset = load_dataset("SakanaAI/Sudoku-Bench", "challenge_100")['test']
    data_source = "SakanaAI/Sudoku-Bench"



    def make_map_fn(split):
        def process_fn(example, idx):
            try:
                puzzle_id = example['puzzle_id']
                author = example['author']
                rules = example['rules']
                rows = example['rows']
                cols = example['cols']
                initial_board = example['initial_board']
                solution = example['solution']
                visual_elements = example['visual_elements']


                initial_board = format_sudoku_board(initial_board)

                if visual_elements is None or visual_elements == "[]":
                    visual_elements = None
                ## pretty visual elements
                if visual_elements is None:
                    pretty_visual_elements = None
                else:
                    visual_elements = json.loads(visual_elements)
                    pretty_visual_elements = pretty_print_visual_elements(visual_elements)
                
                # Construct the prompt
               
                if author is None or author.lower() == 'nikoli':
                    rule_prompt = ONE_SHOT_STANDARD_PROMPT
                else:
                    rule_prompt = ONE_SHOT_VARIANT_PROMPT

                prompt = jinja2.Template(rule_prompt).render(
                    rules=rules,
                    rows=rows,
                    cols=cols,
                    pretty_visual_elements=pretty_visual_elements,
                    current_board=initial_board,
                )

                data = {
                    'data_source': data_source,
                    'prompt': [
                        {
                            'role': 'user',
                            'content': prompt
                        },
                    ],
                    'ability': 'puzzle-solving',
                    'reward_model': {
                        'style': 'rule',
                        'ground_truth': solution,
                    },
                    'extra_info': {
                        'split': split,
                        'index': idx,
                    }
                }
                return data
            except Exception as e:
                pprint(puzzle_id, e)
        return process_fn
    
    # Map the dataset
    processed_train_dataset = train_dataset.map(function=make_map_fn("train"), with_indices=True)
    processed_test_dataset = test_dataset.map(function=make_map_fn("test"), with_indices=True)

    local_dir = args.local_dir
    processed_train_dataset.to_parquet(os.path.join(local_dir, "train.parquet"))
    processed_test_dataset.to_parquet(os.path.join(local_dir, "test.parquet"))

# Login using e.g. `huggingface-cli login` to access this dataset
# df = pd.read_parquet("hf://datasets/SakanaAI/Sudoku-Bench/ctc/test-00000-of-00001.parquet")


# if __name__ == "__main__":
#     #Loop through the DataFrame
#     for index, row in df.iterrows():
        
#         row = row.to_dict()
        
#         rules = row['rules']
#         rows = row['rows']
#         cols = row['cols']

#         initial_board = row['initial_board']
#         initial_board = format_sudoku_board(initial_board)

#         visual_elements = row['visual_elements']
#         if pd.isna(visual_elements) or visual_elements == "[]":
#             visual_elements = None
        
#         ## pretty visual elements
#         if visual_elements is None:
#             pretty_visual_elements = None
#         else:
#             visual_elements = json.loads(visual_elements)
#             pretty_visual_elements = pretty_print_visual_elements(visual_elements)
        
#         # Construct the prompt
#         if row['author'].lower() == 'nikoli':
#             rule_prompt = ONE_SHOT_STANDARD_PROMPT
#         else:
#             rule_prompt = ONE_SHOT_VARIANT_PROMPT
        
#         prompt = jinja2.Template(rule_prompt).render(
#             rules=rules,
#             rows=rows,
#             cols=cols,
#             pretty_visual_elements=pretty_visual_elements,
#             current_board=initial_board,
#         )
#         # Print the prompt
#         print(prompt)
#         break
# 


