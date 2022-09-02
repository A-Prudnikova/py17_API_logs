from voluptuous import Schema
from voluptuous import ALLOW_EXTRA

single_resource = Schema({
    "data": {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str

    }
},
    extra=ALLOW_EXTRA,
    required=True
)

create = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})

update = Schema({
    "name": str,
    "job": str,
    "updatedAt": str
})

delete = Schema({

})

