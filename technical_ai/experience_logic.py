def get_experience_level(years):

    if years <= 2:
        return "0-2"

    elif years <= 5:
        return "3-5"

    return "5+"


if __name__ == "__main__":

    print(get_experience_level(1))
    print(get_experience_level(4))
    print(get_experience_level(8))