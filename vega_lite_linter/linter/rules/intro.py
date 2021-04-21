RuleIntro = {
    "enc_type_valid_1": "Verify the consistency of data field and type 'quantitative'.",
    "enc_type_valid_2": "Verify the consistency of data field and type 'temporal'.",
    "bin_q_o": "Only use bin on quantitative or ordinal data. ",
    "log_q": "Only use log scale with quantitative data.",
    "zero_q": "Only include zero baseline in the scale domain with quantitative data.",
    "log_discrete": "Only use log scale with non-discrete data.",
    "log_zero": "A log scale cannot have a zero baseline in the scale domain.",
    "log_non_positive": "Use log scale on data that are all positive.",
    "bin_and_aggregate": "Use both bin and aggregate on the data in the same time is illegal.",
    "aggregate_o_valid": "Oridnal data only supports min, max, and median aggregation.",
    "aggregate_t_valid": "Temporal only supports min and max.",
    "aggregate_nominal": "Nominal data cannot be aggregated.",
    "count_q_without_field_1": "Use count aggregation or declare a data field of an encoding, instead of doing both of them.",
    "count_q_without_field_2": "The encoding with count aggregation has to be 'quantitative' type.",
    "size_nominal": "Channel size implies order in the data, it is not suitable for nominal data.",
    "size_negative": "Channel size is not suitable for data with negative values.",
    "repeat_channel": "Use each channel only once",
    "no_encodings": "Use at least one encoding. Otherwise, the visualization doesn't show anything.",
    "encoding_no_field_and_not_count": "Declare the data field or use count aggregation in each encoding.",
    "point_tick_bar_without_x_or_y": "Use x or y channel for mark 'point', 'tick', and 'bar'.",
    "line_area_without_x_y": "Use x and y channels for mark 'line' and 'area'.",
    "line_area_with_discrete": "Use no more than one discrete data in x and y channels for mark 'line' and 'area'.",
    "bar_tick_continuous_x_y": "Use no more than one continuous data in the x and y channels for mark 'bar' and 'tick'.",
    "bar_tick_area_line_without_continuous_x_y": "Mark 'bar', 'tick', 'line', 'area' require some continuous variable on x or y.",
    "bar_area_without_zero_1": "Mark 'bar' and 'area' require the scale of x axis to start at zero.",
    "bar_area_without_zero_2": "Mark 'bar' and 'area' require the scale of y axis to start at zero.",
    "size_without_point_text": "Use size channel with mark 'point' would be better.",
    "same_field_x_and_y": "Use different fields for x, and y axises.",
    "count_on_x_and_y": "Use count aggregation in x axis or y axis, instead of both of them.",
    "aggregate_not_all_continuous": "If we use aggregation, then all continuous fields need to be aggeragted.",
    "count_twice": "Use count aggregation once in the visualization.",
    "bar_area_overlap": "Bars and area cannot overlap.",
    "stack_without_bar_area": "Only use stacking for mark 'bar' and 'area'.",
    "stack_without_summative_agg": "Only use summative aggretation (count, sum, distinct, valid, missing) with stack in the encoding.",
    "stack_without_discrete_color_1": "Only use stack with a color channel encoding discrete data in the visualization.",
    "stack_without_discrete_color_2": "Only use stack with a color channel encoding discrete data in the visualization.",
    "stack_without_discrete_color_3": "Only use stack with a color channel encoding discrete data in the visualization.",
    "stack_discrete": "Use stack on continuous data.",
    "stack_without_x_y": "Use stack on x or y channels. ",
    "stack_with_non_positional_non_agg": "When using stack in the visualization, apply aggregation in non-positional continuous channels (color, size) .",
    "color_with_cardinality_gt_twenty": "Use at most 20 categorical colors in the visualization.",
    "invalid_mark": "Use valid mark type, including 'area', 'bar', 'line', 'point', 'tick'.",
    "invalid_channel": "Use valid channels, including x, y, color, size.",
    "invalid_type": "Use valid types, including quantitative, nominal, ordinal, temporal.",
    "invalid_agg": "Use valid aggregation, including count, mean, median, min, max, stdev, sum, etc.",
    "invalid_bin": "Use non-negative number for bin amounts (maxbins)."
}