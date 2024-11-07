MAX_TOKENS = 1024
GPT_3_5_TURBO_MODEL = "gpt-3.5-turbo"
GPT_3_5_TURBO_0301_MODEL = "gpt-3.5-turbo-0301"
GPT_3_5_TURBO_0613_MODEL = "gpt-4o-mini"
GPT_3_5_TURBO_1106_MODEL = "gpt-3.5-turbo-1106"
GPT_3_5_TURBO_0125_MODEL = "gpt-3.5-turbo-0125"
GPT_3_5_TURBO_16K_MODEL = "gpt-3.5-turbo-16k"
GPT_3_5_TURBO_16K_0613_MODEL = "gpt-3.5-turbo-16k-0613"
GPT_4_MODEL = "gpt-4"
GPT_4_0314_MODEL = "gpt-4-0314"
GPT_4_0613_MODEL = "gpt-4-0613"
GPT_4_1106_PREVIEW_MODEL = "gpt-4-1106-preview"
GPT_4_0125_PREVIEW_MODEL = "gpt-4-0125-preview"
GPT_4_TURBO_PREVIEW_MODEL = "gpt-4-turbo-preview"
GPT_4_TURBO_MODEL = "gpt-4-turbo"
GPT_4_TURBO_2024_04_09_MODEL = "gpt-4-turbo-2024-04-09"
GPT_4_32K_MODEL = "gpt-4-32k"
GPT_4_32K_0314_MODEL = "gpt-4-32k-0314"
GPT_4_32K_0613_MODEL = "gpt-4-32k-0613"
GPT_4O_MODEL = "gpt-4o"
GPT_4O_2024_05_13_MODEL = "gpt-4o-2024-05-13"
GPT_4O_MINI_MODEL = "gpt-4o-mini"
GPT_4O_MINI_2024_07_18_MODEL = "gpt-4o-mini-2024-07-18"

# Tuple: (tokens_per_message, tokens_per_name)
MODEL_TOKENS = {
    # GPT-3.5
    GPT_3_5_TURBO_0613_MODEL: (3, 1),
    GPT_3_5_TURBO_16K_0613_MODEL: (3, 1),
    GPT_3_5_TURBO_1106_MODEL: (3, 1),
    GPT_3_5_TURBO_0125_MODEL: (3, 1),
    GPT_3_5_TURBO_0301_MODEL: (
        4,  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        -1,  # if there's a name, the role is omitted
    ),
    # GPT-4
    GPT_4_0314_MODEL: (3, 1),
    GPT_4_32K_0314_MODEL: (3, 1),
    GPT_4_0613_MODEL: (3, 1),
    GPT_4_32K_0613_MODEL: (3, 1),
    GPT_4_1106_PREVIEW_MODEL: (3, 1),
    GPT_4_0125_PREVIEW_MODEL: (3, 1),
    GPT_4_TURBO_PREVIEW_MODEL: (3, 1),
    GPT_4_TURBO_2024_04_09_MODEL: (3, 1),
    # GPT-4o
    GPT_4O_2024_05_13_MODEL: (3, 1),
    # GPT-4o mini
    GPT_4O_MINI_2024_07_18_MODEL: (3, 1),
}

# Note that these fallbacks may change over time.
MODEL_FALLBACKS = {
    GPT_3_5_TURBO_MODEL: GPT_3_5_TURBO_0125_MODEL,
    GPT_3_5_TURBO_16K_MODEL: GPT_3_5_TURBO_16K_0613_MODEL,
    GPT_4_MODEL: GPT_4_0613_MODEL,
    GPT_4_TURBO_MODEL: GPT_4_TURBO_2024_04_09_MODEL,
    GPT_4_32K_MODEL: GPT_4_32K_0613_MODEL,
    GPT_4O_MODEL: GPT_4O_2024_05_13_MODEL,
    GPT_4O_MINI_MODEL: GPT_4O_MINI_2024_07_18_MODEL,
}
