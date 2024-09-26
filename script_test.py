from DataCollector.GPT4oFinetuneDataConverter import FinetuneDataConverter
from Rom.NLPModelSingleton import NLPModelSingleton
from Rom.Rom import Rom, RomComposite
from Rom.RomParser import RomParser
from Rom.tests import Rom_test


def openAI_test():
    import openai

    openai.api_key = ""

    prev_sent = f"previous_sent: Wind-(0, 0) is-(0, 1) the-(0, 2) movement-(0, 3) of-(0, 4) air-(0, 5) from-(0, 6) areas-(0, 7) of-(0, 8) high-(0, 9) pressure-(0, 10) to-(0, 11) areas-(0, 12) of-(0, 13) low-(0, 14) pressure-(0, 15) in-(0, 16) the-(0, 17) Earth-(0, 18) 's-(0, 19) atmosphere-(0, 20). It-(1, 0) is-(1, 1) caused-(1, 2) by-(1, 3) the-(1, 4) uneven-(1, 5) heating-(1, 6) of-(1, 7) the-(1, 8) Earth-(1, 9) 's-(1, 10) surface-(1, 11) by-(1, 12) the-(1, 13) sun-(1, 14) which-(1, 15) creates-(1, 16) temperature-(1, 17) and-(1, 18) pressure-(1, 19) differences-(1, 20). "
    cur_sent = f"current_sent: As-(0, 0) warm-(0, 1) air-(0, 2) rises-(0, 3) cooler-(0, 4) air-(0, 5) moves-(0, 6) in-(0, 7) to-(0, 8) replace-(0, 9) it-(0, 10) creating-(0, 11) air-(0, 12) currents-(0, 13) that-(0, 14) we-(0, 15) experience-(0, 16) as-(0, 17) wind-(0, 18). "

    response = openai.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:concordia-design-lab-analysis::ABoNfvee",
        messages=[
            {
                "role": "system",
                "content": "I will input two sentences. Identify words with the same reference between the first and second sentences and return the result in this format: (index of the first sentence in the text, index of the word in the first sentence, index of the word in the second sentence)."
            },
            {
                "role": "user",
                "content": prev_sent + "\n" + cur_sent
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1

    )

    print(response.choices[0].message.content)

