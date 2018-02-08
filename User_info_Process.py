import label_image_weather

def get_info(flag):
    if flag:
        temperature = float(input('Temperature（℃） :'))
        humidity = float(input('Humidity（0～100|%） :'))
        wind = float(input('Wind （级）:'))
        weather = int(input('Weather （最近是否有雨雪 输入0或1）:')) #rain, snow or not
        visibility = float(input('Visibility （可见距离|km）:'))
        return [temperature, humidity, wind, weather, visibility]
    else:
        return None

def deal_with_info(detection_result, info_list):
    #TODO Build Better Decision Tree
    if detection_result == "fuchen yangsha shachenbao":
        if info_list[2] <= 4:
            return '浮尘'
        elif info_list[-1] <= 1:
            return '沙尘暴'
        else:
            return '扬沙'

    if detection_result == 'mai qingwu wu':
        if info_list[1] <= 80:
            return '霾'
        elif info_list[-1] >10:
            return '轻雾'
        else:
            return '雾'

    if detection_result == 'wusong yusong wuyumix':
        if not info_list[-2]:
            return '雾凇'
        elif info_list[-1] < 10:
            return '雾凇雨凇混合'
        else:
            return '雨凇'

    else:
        return detection_result

if __name__ == '__main__':
    image_path = "/home/vickers_zhu/桌面/timg.jpeg"
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



