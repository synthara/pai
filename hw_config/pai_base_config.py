pai_base = {
    "config_name": "pai_base",

    "rtl_files": [
        "src/axi_pkg.sv",
        # "include/axi/assign.svh",
        # "include/axi/port.svh",
        # "include/axi/typedef.svh",
        "src/axi_intf.sv",
        "src/axi_to_detailed_mem.sv",
        "src/axi_to_mem.sv",
        "src/axi_lite_to_axi.sv",
        "src/axi_lite_from_mem.sv",
        "src/axi_lite_regs.sv",
        "src/axi_to_axi_lite.sv",
        "src/axi_from_mem.sv",
        "src/axi_lite_demux.sv",
        "src/axi_demux.sv",
        "src/axi_err_slv.sv",
        "src/axi_multicut.sv",
        "src/axi_demux_simple.sv",
        "src/axi_lite_mux.sv",
        "src/axi_mux.sv",
        "src/axi_atop_filter.sv",
        "src/axi_burst_splitter.sv",
        "src/axi_cut.sv",
        "src/axi_id_prepend.sv",
        "src/axi_lite_xbar.sv",
        "src/axi_xbar.sv",
    ],

    "rtl_incdirs": ["include", "src"],

    "rtl_dependencies": ["pac_base"],

    "tb_files": [],

    "tb_incdirs": [],

    "tb_dependencies": ["pac_base"], #TODO The TB is based on the old DSL library so it needs ddl as well

    "verilog_wrapper": "",

    "variants": [],
}