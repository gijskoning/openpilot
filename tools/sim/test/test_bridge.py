#!/usr/bin/env python3
import argparse
from multiprocessing import Queue, Process
import unittest
from unittest import mock
from typing import Any

# parser = argparse.ArgumentParser()
# parser.add_argument('--timeout', type=int, default=0)
# args = parser.parse_args()

from tools.sim.bridge import bridge_keep_alive

# # Test connecting to Carla within 1 minute
# q: Any = Queue()
# p = Process(target=bridge_keep_alive, args=(q,), daemon=True)
# p.start()
# p.join(args.timeout + 1)  # to ensure script terminates


class TestBridge(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  @mock.patch('carla.Client')
  def test_starting_bridge(self, mock_client):
    q: Any = Queue()
    bridge_keep_alive(q)

class TestCamerad(unittest.TestCase):
  pass
