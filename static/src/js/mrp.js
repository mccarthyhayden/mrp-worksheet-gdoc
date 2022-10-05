​odoo.define('mrp_worksheet_google_doc.mrp', function (require) {
    "use strict";
    
    var FieldManagerMixin = require('web.FieldManagerMixin');
    
    var LineRenderer = Widget.extend(FieldManagerMixin, {
        _renderCreate: function () { 
            // Copy whole code of _renderCreate method and Paste here. Just change your domain for account_id.
            // Note: Don't call super
        },
    });
    
    return { LineRenderer: LineRenderer, }; 
    
    });