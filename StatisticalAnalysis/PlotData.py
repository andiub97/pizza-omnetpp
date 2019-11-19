import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import math
import logging

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 10)

t95 = 2.086
t90 = 1.725
runs = 20


# Creating CSV and DataFrame
def create_csv(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    for config in [directory for directory in os.listdir(DATA)]:
        config_dir = DATA + '/' + config
        logging.debug(config)
        for file in os.listdir(config_dir):
            file = config_dir + '/' + file
            N = config.replace('First-n', '').replace('Second-n', '').replace('Third-n', '')
            logging.debug('\t' + N + ' - ' + file.replace('.csv', ''))
            if 'Mean' in file:
                with open(file) as file_path:
                    csv_file = pd.read_csv(file)
                    name = csv_file['Name'][0].replace(':mean', '')
                    mean = csv_file['Unnamed: 4'].mean()
                    logging.debug('\t\tMean: ' + str(mean))
                    std_dev = csv_file['Unnamed: 4'].std()
                    logging.debug('\t\tStdDev: ' + str(std_dev))
                    var = csv_file['Unnamed: 4'].var()
                    logging.debug('\t\tVar: ' + str(var))
                    std_err = std_dev / (math.sqrt(runs))
                    logging.debug('\t\tStdErr:' + str(std_err))
                    min_95 = mean - (t95 * math.sqrt(var) / math.sqrt(runs))
                    max_95 = mean + (t95 * math.sqrt(var) / math.sqrt(runs))
                    logging.debug("\t\tMin t95 ConfInt: " + str(min_95) + ' - Max t95 ConfInt: ' + str(max_95))
                    min_90 = mean - (t90 * math.sqrt(var) / math.sqrt(runs))
                    max_90 = mean + (t90 * math.sqrt(var) / math.sqrt(runs))
                    logging.debug("\t\tMin t90 ConfInt: " + str(min_90) + ' - Max t90 ConfInt: ' + str(max_90))
                    data.append([config, name, N, round(mean, 3), round(std_dev, 3), round(var, 3), round(std_err, 3),
                                 round(min_95, 3), round(max_95, 3), round(min_90, 3), round(max_90, 3)])
    df_data = pd.DataFrame(data)
    df_data.columns = ['Config', 'Name', 'N', 'Mean', 'Std Dev', 'Var', 'Std Err', 'Min ConfInt t95', 'Max ConfInt t95',
                       'Min ConfInt t90', 'Max ConfInt t90']
    for n in range(0, 12):
        df_data.at[(n * 5) + 1, 'Name'] = 'queueLengthU2'
        df_data.at[(n * 5) + 3, 'Name'] = 'queueLengthU1'

    df_data = df_data.sort_values(by=['Config', 'Name'], ascending=True)
    logging.debug(df_data)
    logging.info(df_data.head())

    df_data.to_csv('./Total_Data_Mean.csv', index=False)
    return df_data


def create_plot_conf(df, DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)

    # DataFrame per Name type
    life_time = df[df['Name'].isin({'lifeTime'})]
    life_time_u1 = df[df['Name'].isin({'lifeTimeU1'})]
    life_time_u2 = df[df['Name'].isin({'lifeTimeU2'})]
    queue_length_u1 = df[df['Name'].isin({'queueLengthU1'})]
    queue_length_u2 = df[df['Name'].isin({'queueLengthU2'})]

    # Plot Parameters
    N = 4
    width = 0.25

    for df_type in life_time, life_time_u1, life_time_u2, queue_length_u1, queue_length_u2:
        measure = df_type.iloc[0]['Name']
        configuration = ['First', 'Second', 'Third']
        for n in range(3):
            fig_95, ax = plt.subplots()
            ind = np.arange(N)
            low_bound_95 = ax.bar(ind+width, df_type['Min ConfInt t95'][n:n + 4], width, bottom=0)
            mean = ax.bar(ind + 2*width, df_type['Mean'][n:n + 4], width, bottom=0)
            high_bound_95 = ax.bar(ind + 3 * width, df_type['Max ConfInt t95'][n:n + 4], width, bottom=0)
            space = ax.bar(ind + 4 * width, np.asarray([0., 0., 0., 0.]), width, bottom=0)
            ax.set_title(configuration[n] + ' Configuration - ' + measure + ' - t=90')
            ax.set_xticks((ind + 3 * width / 2))
            ax.set_xticklabels(('2', '3', '4', '5'))
            ax.legend((low_bound_95[0], mean[0], high_bound_95[0]), ('Low Bound 90', 'Mean', 'High Bound'))
            ax.autoscale_view()
            plt.savefig('./charts/'+DATA+'/ConfInt_95/' + configuration[n]+'_'+measure+'_90')
            plt.show()

            fig_90, bx = plt.subplots()
            ind = np.arange(N)
            low_bound_90 = bx.bar(ind + width, df_type['Min ConfInt t90'][n:n + 4], width, bottom=0)
            mean_90 = bx.bar(ind + 2 * width, df_type['Mean'][n:n + 4], width, bottom=0)
            high_bound_90 = bx.bar(ind + 3 * width, df_type['Max ConfInt t90'][n:n + 4], width, bottom=0)
            space = bx.bar(ind + 4 * width, np.asarray([0., 0., 0., 0.]), width, bottom=0)
            bx.set_title(configuration[n] + ' Configuration - ' + measure)
            bx.set_xticks((ind + 3 * width / 2))
            bx.set_xticklabels(('2', '3', '4', '5'))
            bx.legend((low_bound_90[0], mean_90[0], high_bound_90[0]), ('Low Bound', 'Mean', 'High Bound'))
            bx.autoscale_view()
            plt.savefig('./charts/'+DATA+'/ConfInt_90/' + configuration[n] + '_' + measure +'_90')
            plt.show()


if __name__ == "__main__":
    df_obj_data = create_csv('./data',logging.INFO)
    create_plot_conf(df_obj_data, 'data', logging.INFO)
    df_obj_data_no_transient = create_csv('./data_no_transient', logging.INFO)
    create_plot_conf(df_obj_data_no_transient, 'data_no_transient', logging.INFO)
