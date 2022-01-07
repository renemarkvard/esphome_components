import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

genvex_ns = cg.esphome_ns.namespace('genvex')
Genvex = genvex_ns.class_('Genvex', cg.Component)

CONF_NILAN_ID = 'genvex_id'

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Genvex),
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config) 
