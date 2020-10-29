import matplotlib.pyplot as plt


class Experiments:
    def __init__(self):
        self.experiments = []

    def add(self, func, args_lists, search_method='grid', tex=True, plot=True):
        self.experiments.append((func, args_lists, search_method, plot))

    def run(self, verbose=True):
        experiment_results = []
        for func, args_lists, search_method, plot in self.experiments:
            results = []
            current_params_idxs = [0]*len(args_lists)
            if search_method == 'grid':
                while current_params_idxs[0] < len(args_lists[0]):
                    current_params = [args[current_params_idxs[ai]] for ai, args in enumerate(args_lists)]
                    output = func(*current_params)
                    results.append((current_params, output))

                    # shift
                    current_params_idxs[-1] += 1
                    for i in range(len(current_params_idxs)-1, 0, -1):
                        if current_params_idxs[i] >= len(args_lists[i]):
                            current_params_idxs[i] = 0
                            current_params_idxs[i-1] += 1
            experiment_results.append(results)

            if plot:
                plt.plot(*zip(*results))
                #plt.savefig('images/')
        self.generate(experiment_results)
        return experiment_results

    def generate(self, experiment_results):
        with open('main.tex', 'w') as file:
            for experiment in experiment_results:
                for params, output in experiment:
                    file.write(str(params) + ' ' + str(output) + '\n')
