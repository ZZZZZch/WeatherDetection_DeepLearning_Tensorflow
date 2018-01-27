import label_image_weather

def get_info(flag):
    if flag:
        temperature = input('Temperature :')
        humidity = input('Humidity :')
        wind = input('Wind :')
        weather = input('Weather :') #rain, snow or not
        visibility = input('Visibility :')
        return [temperature, humidity, wind, weather, visibility]
    else:
        return None

def deal_with_info(detection_result, info_list):
    #TODO Build Better Decision Tree
    if detection_result == "fuchen yangsha shachenbao":
        if info_list[2] <= 4:
            return 'FuChen'
        elif info_list[-1] <= 1:
            return 'ShaChenBao'
        else:
            return 'YangSha'

    if detection_result == 'mai qingwu wu':
        if info_list[1] <= 80:
            return 'Mai'
        elif info_list[-1] >10:
            return 'QingWu'
        else:
            return 'Wu'

    if detection_result == 'wusong yusong wuyumix':
        if not info_list[-2]:
            return 'WuSong'
        elif info_list[-1] < 10:
            return 'WuYuMix'
        else:
            return 'YuSong'

    else:
        return detection_result

if __name__ == '__main__':
    image_path = "4118964.jpg"
    model_path_without_flag = './models_labels/weather_output_without_info.pb'
    label_path_without_flag  = './models_labels/output_labels_without_info.txt'
    model_path_with_flag = './models_labels/output_graph_with_info.pb'
    label_path_with_flag = './models_labels/output_labels_with_info.txt'
    flag = int(input('Do you have some info to tell us?(1/0):  '))

    info_list = get_info(flag)

    if not info_list:
        print('Begin Detection...')
        pre_result = label_image_weather.run(image_path, model_path_without_flag,
                                             label_path_without_flag)

        print('Here is our result :', pre_result[0][0], pre_result[0][1])

    else:
        print('Begin Detection...')
        pre_result = label_image_weather.run(image_path, model_path_with_flag,
                                             label_path_with_flag)
        result = pre_result[0][0]
        final_result = deal_with_info(result, info_list)
        print('Here is our result :', final_result)



