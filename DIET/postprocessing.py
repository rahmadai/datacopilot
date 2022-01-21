def post_processing_entity(text, first_idx_entity, last_idx_entity):
    word_list = text.split(" ")
    result = []

    numbers_of_index = [
        item for item in range(first_idx_entity, last_idx_entity + 1, +1)
    ]

    idx_word_first = 0
    idx_word_last = 0
    for i, word in enumerate(word_list):
        if i == 0:
            idx_word_first = 0
            idx_word_last = len(word) - 1
        else:
            idx_word_first = idx_word_last + 2
            idx_word_last += len(word) + 1

        for j, number in enumerate(numbers_of_index):
            # if number == idx_word_first - 1:
            #     if word not in result:
            #         result.append(word_list[i])
            #     break

            if idx_word_first <= number and number <= idx_word_last:
                if word not in result:
                    result.append(word)
                break
    return " ".join(result)


def post_processing(result):
    entities = result["entities"]
    for i, entity in enumerate(entities):
        entity_post = post_processing_entity(
            result["text"], entity["start"], entity["end"]
        )
        result["entities"][i]["value"] = entity_post

    return result


# print(y)
print(post_processing(x))
