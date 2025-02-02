#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


class AffineEncoder(object):
    def __init__(self, mult=2 ** 100, trans=0):
        self.mult = mult
        self.trans = trans

    def encode(self, plaintext):
        return int(self.mult * (plaintext + self.trans))

    def decode(self, ciphertext, multiplier=1, mult_times=0):
        for i in range(mult_times + 1):
            ciphertext /= self.mult
        return ciphertext - multiplier * self.trans
        # return ciphertext / self.mult - multiplier * self.trans
