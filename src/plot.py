import matplotlib.pyplot as plt
import csv

def choose_plotting_function(plotting_function, csv_file_name) -> None:
    if plotting_function == 'mouse':
        plot_mouse_graph(csv_file_name)
    if plotting_function == 'chase':
        plot_chase_graph(csv_file_name)
    if plotting_function == 'metric':
        plot_metric(csv_file_name)
    else:
        return None

def plot_metric(csv_file_name: str) -> None:
    # Initialize lists to store the fitness values
    number_of_cheeses = []
        
    # Open the input file and read the data
    with open("csv_data/{}".format(csv_file_name), 'r') as input_file:
        # Process each row in the CSV file
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            number_of_cheeses.append(float(row[1]))

    # Plot the fitness values
    generations = range(1, len(number_of_cheeses) + 1)

    # Create a figure and two axes objects
    fig, ax1 = plt.subplots(figsize=(18, 8))

    # Plot the first set of data on the first y-axis
    ax1.plot(generations, number_of_cheeses, label='Total Number of Cheeses', color='blue')

    ax1.set_xlabel('Generations')
    ax1.set_ylabel('Total Number of cheeses')

    ax1.set_ylim([0, 100])

    ax1.tick_params('y', colors='blue')


    # Add legends for the two plots
    lines1, labels1 = ax1.get_legend_handles_labels()
    ax1.legend(lines1, labels1, loc='upper center', bbox_to_anchor=(0.5, 1.07), ncol=4, frameon=False, prop={'size': 14})

    file_name = csv_file_name[:-4]

    ax1.margins(x=0)

    ax1.title.set_fontsize(18)
    ax1.xaxis.label.set_fontsize(18)
    ax1.yaxis.label.set_fontsize(18)
 
    #save graph to directory
    plt.savefig('plots/{}.png'.format(file_name))

    # Display the plot
    plt.show()


def plot_chase_graph(csv_file_name: str) -> None:
    # Initialize lists to store the fitness values
    prey_average_fitness = []
    prey_best_fitness = []

    predator_average_fitness = []
    predator_best_fitness = []
        
    # Open the input file and read the data
    with open("csv_data/{}".format(csv_file_name), 'r') as input_file:
        # Process each row in the CSV file
        csv_reader = csv.reader(input_file)
        line_counter = 1
        for row in csv_reader:
            if line_counter % 2 == 0:
                prey_average_fitness.append(float(row[1]))
                prey_best_fitness.append(float(row[2]))
            else:
                predator_average_fitness.append(float(row[1]))
                predator_best_fitness.append(float(row[2]))
            
            line_counter = line_counter + 1



    # Plot the fitness values
    generations = range(1, len(predator_average_fitness) + 1)

    # Create a figure and two axes objects
    fig, ax1 = plt.subplots(figsize=(18, 8))
    ax2 = ax1.twinx()

    # Plot the first set of data on the first y-axis
    ax1.plot(generations, prey_average_fitness, label='Prey Average fitness', color='blue')
    ax1.plot(generations, prey_best_fitness, label='Prey Best fitness', color='red', linestyle='dotted')

    ax1.set_xlabel('Generations')
    ax1.set_ylabel('Prey Fitness')

    ax1.set_ylim([0, 1])

    ax1.tick_params('y', colors='blue')

    # Plot the second set of data on the second y-axis
    ax2.plot(generations, predator_average_fitness, label='Predator Average fitness', color='green')
    ax2.plot(generations, predator_best_fitness, label='Predator Best fitness', color='purple', linestyle='dotted')

    ax2.set_ylabel('Predator Fitness')

    ax2.set_ylim([0, 30])

    ax2.tick_params('y', colors='green')

    # Add legends for the two plots
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.07), ncol=4, frameon=False, prop={'size': 14})

    plt.title('Fitness over generations', y=1.08)

    file_name = csv_file_name[:-4]

    ax1.margins(x=0)
    ax2.margins(x=0)

    ax1.title.set_fontsize(18)
    ax1.xaxis.label.set_fontsize(18)
    ax1.yaxis.label.set_fontsize(18)


    ax2.title.set_fontsize(18)
    ax2.yaxis.label.set_fontsize(18)
 
 
    #save graph to directory
    plt.savefig('plots/{}.png'.format(file_name))

    # Display the plot
    plt.show()






def plot_mouse_graph(csv_file_name: str) -> None:
    # Initialize lists to store the fitness values
    average_fitness = []
    best_fitness = []
        
    # Open the input file and read the data
    with open("csv_data/{}".format(csv_file_name), 'r') as input_file:
        # Process each row in the CSV file
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            average_fitness.append(float(row[1]))
            best_fitness.append(float(row[2]))


    # Plot the fitness values
    generations = range(1, len(average_fitness) + 1)
    plt.plot(generations, average_fitness, label='Average fitness')
    plt.plot(generations, best_fitness, label='Best fitness')

    # Add labels and a legend to the plot
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness over generations')
    plt.legend()


    file_name = csv_file_name[:-4]
    #save graph to directory
    plt.savefig('plots/{}.png'.format(file_name))

    # Display the plot
    plt.show()
