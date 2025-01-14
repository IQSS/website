/**
 * Copyright 2023 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import styled from "styled-components";
import { SDG_ICON_URL } from "../../../utils/constants";
import {
  ContentCard,
  ContentCardHeader,
  MainLayoutContent,
} from "../components";

const StyledContentCardHeader = styled(ContentCardHeader)`
  margin-bottom: 0;
`;

const AllGoalsOverview = () => {
  return (
    <MainLayoutContent className="-dc-goal-overview -dc-goal-overview-all">
      <ContentCard>
        <StyledContentCardHeader>
          <img src={SDG_ICON_URL} />
          <h3>All Goals</h3>
        </StyledContentCardHeader>
      </ContentCard>
    </MainLayoutContent>
  );
};

export default AllGoalsOverview;
