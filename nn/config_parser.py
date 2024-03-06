

def parse_config( config_file_path ) :
	config = []
	default = {"weight_mutate_rate": 0.5, "elitist_reproduction_coefficient" : 0.5, "weight_replace_rate": 0.1, "fitness_criterion": 100, "population_size": 1000, "survival_threshhold": 0.5, "weight_mutate_power": 0.5, "weight_replace_rate": 0.1, "weight_max": 30, "weight_min": -30, "bias_mutate_rate": 0.3, "bias_mutate_power": 0.5, "bias_replace_rate": 0.1, "bias_max": 30, "bias_min": -30, "response_max": 30, "response_min": -30, "activation_mutate_rate": 0.1, "activation_default": "sigmoid", "activation_options": ["relu", "sigmoid", "tanh"]}
	f = open(config_file_path, "r")
	lines = f.readlines()
	for line in lines:
		if "#" != line[0]:
			splitline = line.split(" ")
			if len(splitline) != 1:
				if len(splitline) == 2:
					if splitline[0] != 'activation_default':
						default[splitline[0]] = float(splitline[1].replace("\n", ""))
					else: 
						default[splitline[0]] = splitline[1].replace("\n", "")

				else:
					default[splitline[0]] = [word.replace("\n", "") for word in splitline[1::]]
	return default



