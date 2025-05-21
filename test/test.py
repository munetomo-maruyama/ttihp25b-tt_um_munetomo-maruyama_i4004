#//===========================================================
#// MCS-4 Project
#//-----------------------------------------------------------
#// File Name   : test.py
#// Description : Cocotb of MCS-4 System
#//-----------------------------------------------------------
#// History :
#// Rev.01 2025.05.21 M.Maruyama First Release
#//-----------------------------------------------------------
#// Copyright (C) 2025 M.Maruyama
#//===========================================================
# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 1333 ns (750 KHz)
    clock = Clock(dut.tb_clk, 1333, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.tb_res.value = 1
    dut.enable_keyprt.value = 1
    await ClockCycles(dut.tb_clk, 10)
    dut.tb_res.value = 0

    dut._log.info("Simulation of 141-PF Calculator")
    await ClockCycles(dut.tb_clk, 50000)
    
    # Key Input
    dut.port_keyprt_cmd.value = 0x0000009b # 1
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000097 # 2
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off    
    await ClockCycles(dut.tb_clk, 50000)

    dut.port_keyprt_cmd.value = 0x0000008e # +
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)

    dut.port_keyprt_cmd.value = 0x00000093 # 3
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x0000009a # 4
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)
    
    dut.port_keyprt_cmd.value = 0x0000008e # +
   #dut.port_keyprt_cmd.value = 0x0000008d # -
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)

    dut.port_keyprt_cmd.value = 0x0000008c # =
    await ClockCycles(dut.tb_clk, 50000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 50000)

    dut.port_keyprt_cmd.value = 0x00008000 # FIFO POP
    await ClockCycles(dut.tb_clk, 4)
    assert dut.port_keyprt_res.value == 0x80000001
    await ClockCycles(dut.tb_clk, 10000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 10000)

    dut.port_keyprt_cmd.value = 0x00008000 # FIFO POP
    await ClockCycles(dut.tb_clk, 4)
    assert dut.port_keyprt_res.value == 0x80008401
    await ClockCycles(dut.tb_clk, 10000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 10000)

    dut.port_keyprt_cmd.value = 0x00008000 # FIFO POP
    await ClockCycles(dut.tb_clk, 4)
    assert dut.port_keyprt_res.value == 0x80010801
    await ClockCycles(dut.tb_clk, 10000)
    dut.port_keyprt_cmd.value = 0x00000000 # off
    await ClockCycles(dut.tb_clk, 10000)
    
    await ClockCycles(dut.tb_clk, 1000000)

#//===========================================================
# End of File
#//===========================================================
