import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import os
import math
import logging

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 10)

t95 = 2.086
t90 = 1.725
runs = 20


# Creating CSV and DataFrame
def create_csv_mean(DATA, log_level):
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
    logging.debug(df_data.head())

    df_data.to_csv('./data/Total_Data_Mean.csv', index=False)
    logging.info('CSV MEAN CREATED ' + DATA.replace('./', ''))
    return df_data


def create_csv_lifetime(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    for config in [directory for directory in os.listdir(DATA)]:
        config_dir = DATA + '/' + config
        logging.debug(config)
        for file in os.listdir(config_dir):
            file = config_dir + '/' + file
            N = config.replace('First-n', '').replace('Second-n', '').replace('Third-n', '')
            logging.debug('\t' + N + ' - ' + file.replace('.csv', ''))
            if 'LifeTime' in file:
                csv_file = pd.read_csv(file)
                name = csv_file['Name'][0]
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

    df_data = df_data.sort_values(by=['Config', 'Name'], ascending=True)
    logging.debug(df_data)

    df_data.to_csv('./data/Total_Data_LifeTime.csv', index=False)
    logging.info('CSV LIFETIME CREATED ' + DATA.replace('./', ''))
    return df_data


def create_csv_queue(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    for config in [directory for directory in os.listdir(DATA)]:
        config_dir = DATA + '/' + config
        logging.debug(config)
        for file in os.listdir(config_dir):
            file = config_dir + '/' + file
            N = config.replace('First-n', '').replace('Second-n', '').replace('Third-n', '')
            logging.debug('\t' + N + ' - ' + file.replace('.csv', ''))
            if 'EntryQueueLength' in file:
                csv_file = pd.read_csv(file)
                name = csv_file['Name'][0]
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

    df_data = df_data.sort_values(by=['Config', 'Name'], ascending=True)
    logging.debug(df_data)

    df_data.to_csv('./data/Total_Data_QueueLength.csv', index=False)
    logging.info('CSV QUEUELENGTH CREATED ' + DATA.replace('./', ''))
    return df_data


def create_plot_conf(df, DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    print(df)
    # DataFrame per Name type
    life_time = df[df['Name'].isin({'lifeTime'})]
    life_time_u1 = df[df['Name'].isin({'lifeTimeU1'})]
    life_time_u2 = df[df['Name'].isin({'lifeTimeU2'})]
    queue_length_u1 = df[df['Name'].isin({'queueLengthU1'})]
    queue_length_u2 = df[df['Name'].isin({'queueLengthU2'})]
    # for df in life_time, life_time_u1, life_time_u2, queue_length_u1, queue_length_u2:
    #     print(df)
    # Plot Parameters
    N = 4
    width = 0.25

    for df_type in life_time, life_time_u1, life_time_u2, queue_length_u1, queue_length_u2:
        measure = df_type.iloc[0]['Name']
        configuration = ['First', 'Second', 'Third']
        for n in range(3):
            fig_95, ax = plt.subplots()
            ind = np.arange(N)
            low_bound_95 = ax.bar(ind + width, df_type['Min ConfInt t95'][n:n + 4], width, bottom=0)
            mean = ax.bar(ind + 2 * width, df_type['Mean'][n:n + 4], width, bottom=0)
            high_bound_95 = ax.bar(ind + 3 * width, df_type['Max ConfInt t95'][n:n + 4], width, bottom=0)
            space = ax.bar(ind + 4 * width, np.asarray([0., 0., 0., 0.]), width, bottom=0)
            ax.set_title(configuration[n] + ' Configuration - ' + measure + ' - t=90')
            ax.set_xticks((ind + 3 * width / 2))
            ax.set_xticklabels(('2', '3', '4', '5'))
            ax.legend((low_bound_95[0], mean[0], high_bound_95[0]), ('Low Bound 90', 'Mean', 'High Bound'))
            ax.autoscale_view()
            plt.savefig(DATA + '/ConfInt_95/' + configuration[n] + '_' + measure + '_90')
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
            plt.savefig(DATA + '/ConfInt_90/' + configuration[n] + '_' + measure + '_90')
            plt.show()
    logging.info('CHARTS CONF-INT CREATED ' + DATA)


def create_plot_lifetime(df, DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)

    # DataFrame per Name type
    life_time = df[df['Name'].isin({'lifeTime:mean', 'lifeTime:max', 'lifeTime:min'})]
    logging.info(life_time)
    life_time_u1 = df[df['Name'].isin({'lifeTimeU1:mean', 'lifeTimeU1:max', 'lifeTimeU1:min'})]
    life_time_u2 = df[df['Name'].isin({'lifeTimeU2:mean', 'lifeTimeU2:max', 'lifeTimeU2:min'})]

    # Plot Parameters
    N = [2, 3, 4, 5]

    for df_type in life_time, life_time_u1, life_time_u2:
        measure = df_type.iloc[0]['Name'].replace(':max', '').replace(':mean', '').replace(':min', '')
        for config in 'First', 'Second', 'Third':
            fig_lifetime, ax = plt.subplots()
            maxs = []
            means = []
            mins = []
            for N_val in N:
                df_triplet = df_type[df_type['Config'].isin({config + '-n' + str(N_val)})]
                maxs.append(round(df_triplet.iloc[0]['Mean']))
                means.append(round(df_triplet.iloc[1]['Mean']))
                mins.append(round(df_triplet.iloc[2]['Mean']))
            max_plt = ax.plot(N, maxs)
            mean_plt = ax.plot(N, means)
            min_plt = ax.plot(N, mins)
            ax.set_title(config + ' Configuration - ' + measure)
            ax.legend((max_plt[0], mean_plt[0], min_plt[0]), ('Max LifeTime', 'Mean LifeTime', 'Min LifeTime'))
            ax.autoscale_view()
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            plt.savefig(DATA + '/LifeTime/' + config + '_' + measure)
            plt.show()
    logging.info('CHARTS LIFETIME CREATED ' + DATA)


def create_plot_queuelength(df, DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)

    # DataFrame per Name type
    queue_length = df[df['Name'].isin({'queueLength:mean'})]

    # Plot Parameters
    N = [2, 3, 4, 5]

    measure = queue_length.iloc[0]['Name'].replace(':max', '').replace(':mean', '').replace(':min', '')
    for config in 'First', 'Second', 'Third':

        queue_length1 = []
        queue_length2 = []
        queue_length_mean = []
        for N_val in N:
            df_i = queue_length[queue_length['Config'].isin({config + '-n' + str(N_val)})]
            queue_length2.append(round(df_i.iloc[0]['Mean']))
            queue_length1.append(round(df_i.iloc[1]['Mean']))
            queue_length_mean.append(round((df_i.iloc[0]['Mean']+df_i.iloc[1]['Mean'])/2))

        fig, ax = plt.subplots()
        ax.plot(N, queue_length_mean)
        ax.set_title(config + ' Configuration - ' + measure + ' Mean')
        ax.autoscale_view()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(DATA + '/QueueLength/' + config + '_' + measure + '_Mean')
        # plt.show()

        fig, bx = plt.subplots()
        bx.plot(N, queue_length1)
        bx.set_title(config + ' Configuration - ' + measure + ' U1')
        bx.autoscale_view()
        bx.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(DATA + '/QueueLength/' + config + '_' + measure + '_U1')
        # plt.show()

        fig, cx = plt.subplots()
        cx.plot(N, queue_length2)
        cx.set_title(config + ' Configuration - ' + measure + ' U2')
        cx.autoscale_view()
        cx.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.savefig(DATA + '/QueueLength/' + config + '_' + measure + '_U2')
        # plt.show()

        plt.cla()
        plt.clf()
        plt.close(fig)

    logging.info('CHARTS LIFETIME CREATED ' + DATA)


if __name__ == "__main__":
    # Extract data results with transient
    df_data_mean = create_csv_mean('./data/data_results', logging.INFO)
    df_data_lifetime = create_csv_lifetime('./data/data_results', logging.INFO)
    df_data_queue_mean = create_csv_queue('./data/data_results', logging.INFO)
    create_plot_conf(df_data_mean, './charts/charts_results', logging.INFO)
    create_plot_lifetime(df_data_lifetime, './charts/charts_results', logging.INFO)
    create_plot_queuelength(df_data_queue_mean, './charts/charts_results', logging.INFO)

    # Extract data results without transient
    df_data_mean_no_transient = create_csv_mean('./data/data_results_no_transient', logging.INFO)
    df_data_lifetime_no_transient = create_csv_lifetime('./data/data_results_no_transient', logging.INFO)
    df_data_queue_mean_no_transient = create_csv_queue('./data/data_results_no_transient', logging.INFO)
    create_plot_conf(df_data_mean_no_transient, './charts/charts_results_no_transient', logging.INFO)
    create_plot_lifetime(df_data_lifetime_no_transient, './charts/charts_results_no_transient', logging.INFO)
    create_plot_queuelength(df_data_queue_mean_no_transient, './charts/charts_results_no_transient', logging.INFO)