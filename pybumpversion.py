#!/usr/bin/env python3
import argparse
import logging

from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format='[%(asctime)s|%(levelname)s|%(module)s|%(lineno)d] %(message)s')
logger = logging.getLogger(__name__)

def bump_version(current_version, datetime):
    reset_build_num = False
    current_year, current_month, current_build_num = current_version.split('.')
    new_year = str(datetime.year)[:2]

    if current_year != new_year or int(current_month) != datetime.month:
        reset_build_num = True

    if reset_build_num:
        new_build_num = 0
    else:
        new_build_num = int(current_build_num) + 1

    new_version = f'{new_year}.{datetime.month:02d}.{new_build_num:04d}'
    return new_version

def clean_current_version(line):
    strip_chars = ['"', "'", ' ', '\n']
    cleaned = line.split('=')[1]
    for char in strip_chars:
        cleaned = cleaned.replace(char, '')
    return cleaned

def main(version_file):
    logger.info(f'Bumping version using file {version_file}')
    utc_now = datetime.now(timezone.utc)
    lines = open(version_file).readlines()
    for index, line in enumerate(lines):
        if '__version__' in line:
            current_version = clean_current_version(line)
            new_version = bump_version(current_version, utc_now)
            logger.info(f'Current version: {current_version}')
            logger.info(f'New version: {new_version}')
            lines[index] = f"__version__ = '{new_version}'\n"

    logger.info(f'Writing new version to file: {version_file}')
    open(version_file, 'w').writelines(lines)
    logger.info('Done.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('version_file')

    args = parser.parse_args().__dict__
    main(**args)
