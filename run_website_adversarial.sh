#!/bin/bash
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e

export GOOGLE_CLOUD_PROJECT=datcom-website-dev

python3 -m venv .env
source .env/bin/activate
pip3 install -r server/requirements.txt

# copy input files
mkdir -p input
gsutil cp gs://datcom-website-adversarial/input/frequent/* input/

# Define a list of domains
domain_list=(dev.datacommons.org)

# Loop through the domain list
for domain in "${domain_list[@]}"
do
  date_str=$(TZ="America/Los_Angeles" date +"%Y_%m_%d_%H_%M_%S")
  python3 server/integration_tests/standalone/adversarial.py --mode=run_all --base_url="https://$domain"
  gsutil cp ./output/reports/* gs://datcom-website-adversarial/reports/$domain/$date_str/
  rm -rf ./input/*
  rm -rf ./output/*
done
