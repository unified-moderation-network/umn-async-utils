#   Copyright 2020-present Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


__version__ = "1.5.0"

__all__ = (
    "__version__",
    "PriorityLock",
    "RateLimiter",
    "Scheduler",
    "Waterfall",
    "priority",
    "taskcache",
)


from ._prioritylock import PriorityLock, priority
from ._ratelimiter import RateLimiter as RateLimiter
from ._scheduler import Scheduler as Scheduler
from ._task_cache import taskcache as taskcache
from ._waterfall import Waterfall as Waterfall