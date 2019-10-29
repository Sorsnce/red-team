local io = require "io"
local string = require "string"
local table = require "table"

table.insert(fingerprints, {
    category = 'general',
    probes = {
{path='/index/',method = 'HEAD'},
{path='/images/',method = 'HEAD'},
{path='/download/',method = 'HEAD'},
{path='/css/',method = 'HEAD'},
{path='/manual/',method = 'HEAD'},
{path='/fonts/',method = 'HEAD'},
{path='/moodle/',method = 'HEAD'},
},
    matches = {
      {
        match = '',
        output = 'Please Investigate'
      }
    }
  });
