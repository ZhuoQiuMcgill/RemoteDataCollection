import os
import pandas as pd
import json


class FinetuneDataConverter:
    def __init__(self,
                 input_csv_path=os.path.join("data", "finetuneData", "finetune_data.csv"),
                 output_json_path=os.path.join("data", "finetuneData", "finetune_data.jsonl")):
        self.input_csv_path = input_csv_path
        self.output_json_path = output_json_path
        self.system_prompt = "I will input two sentences. Identify words with the same reference between the first " \
                             "and second sentences and return the result in this format: (index of the first sentence " \
                             "in the text, index of the word in the first sentence, index of the word in the second " \
                             "sentence)."

    def convert(self):
        # 读取CSV文件
        data = pd.read_csv(self.input_csv_path)
        finetune_data = []

        # 遍历每一行，将其转换为指定格式
        for _, row in data.iterrows():
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"previous_sent: {row['PREVIOUS_TEXT']}\ncurrent_sent: {row['CURRENT_TEXT']}"},
                {"role": "assistant", "content": f"{row['MAPPING_DATA']}"}
            ]
            finetune_data.append({"messages": messages})

        # 将数据保存为JSON Lines格式
        with open(self.output_json_path, 'w', encoding='utf-8') as json_file:
            for entry in finetune_data:
                json.dump(entry, json_file, ensure_ascii=False)
                json_file.write('\n')

        print(f"Data successfully saved to {self.output_json_path}")
