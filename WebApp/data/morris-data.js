$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{int:"0", alpha:0.18813944428612306, beta:0.2262564283608129,  delta:0.11721854089904465,gamma:0.13713617078478516,R:0.6702497836930253},{int:"1", alpha:0.15611176847623565, beta:0.16857886570077182, delta:0.1011998086367383, gamma:0.22519892053866175, R:0.6801623117253518}, 
{int:"2", alpha:0.1844953379753076,  beta:0.20060858215920552, delta:0.12736809750860417,gamma:0.1429408672275284, R:0.702377624591468},
{int:"3", alpha:0.16220328266438355, beta:0.1746300440389687,  delta:0.13398491318059938,gamma:0.16407072659191752, R:0.6854452352566562}, 
{int:"4", alpha:0.16220328266438355, beta:0.1746300440389687,  delta:0.13398491318059938,gamma:0.16407072659191752, R:0.6854452352566562}, 
{int:"5", alpha:0.16220328266438355, beta:0.1746300440389687,  delta:0.13398491318059938,gamma:0.16407072659191752, R:0.6854452352566562}, 
{int:"6", alpha:0.16220328266438355, beta:0.1746300440389687,  delta:0.13398491318059938,gamma:0.16407072659191752, R:0.6854452352566562}, 
{int:"7", alpha:0.18099115533997204, beta:0.13380971603775682, delta:0.10118282102452232,gamma:0.2743715975895481, R:1.0142866914629773}, 
{int:"8", alpha:0.17380264158204603, beta:0.13932405411358034, delta:0.13840833573568703,gamma:0.24284396260533148, R:0.9297820681014125}],
        xkey: 'int',
        ykeys: ['alpha', 'beta','delta','gamma','R'],
        labels: ['alpha', 'beta', 'delta','gamma','R'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Focused",
            value: 12
        }, {
            label: "Lightly Focused",
            value: 18
        },{
            label: "Medium Focused",
            value: 20
        },{
            label: "Highly Focused",
            value: 30
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            Page: '1',
            alpha: 15.611176847623565,
            t: 2
        }, {
            Page: '2',
            alpha: 18.44953379753076,
            t: 27
        }, {
            Page: '3',
            alpha: 16.220328266438355,
            t: 17
        }, {
            Page: '4',
            alpha: 16.220328266438355,
            t: 27
        }, {
            Page: '5',
            alpha: 16.220328266438355,
            t: 23
        }, {
            Page: '6',
            alpha: 16.220328266438355,
            t: 24
        }, {
            Page: '7',
            alpha: 18.099115533997204,
            t: 11
        }],
        xkey: 'Page',
        ykeys: ['alpha', 't'],
        labels: ['Alpha %', 'Time Spend'],
        hideHover: 'auto',
        resize: true
    });
    
});
