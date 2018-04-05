"""
Memory profiling (line by line) for the preprocessing step

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run preprocess_memory.py PATH_TO_CONFIG_FILE

Plot results:

mprof plot
"""
import logging
import argparse
from datetime import datetime
from memory_profiler import profile
import yass
from yass import preprocess


if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    start = datetime.now()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=str,
                        help="Path to config file")
    parser.add_argument("-l", "--logger", type=str,
                        help="YASS logger level",
                        default="WARNING")
    args = parser.parse_args()

    # configure logs from yass
    logging.getLogger("yass").setLevel(args.logger)
    # logs from this script
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(__name__)

    # set yass configuration parameters
    yass.set_config(args.config)

    logger.info('Preprocessing started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # preprocessing
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = profile(preprocess.run)(if_file_exists='overwrite')

    logger.info('Preprocessing finished at second: %.2f',
                (datetime.now() - start).total_seconds())
