a = {'date'              '080415f'    'na'
    'lengtrecording'    '1.6'        's' 
    'samplerate'        '0.95'       'Hz'
    'Amplitude'         '1'          'V' 
    'Pulse_period'      '20'         'ms'
    'Pulse_numbers'     '10'         'na'
    'Cell_period'       '10'         's' 
    'Cell_numbers'      '10'         'na'
    'framerate'         '10000'      'Hz'}
 
str = strcat(a[:,1],{' : '},a[:,2],{' ('},a[:,3],{')'});
 
figure
uicontrol('style','text',...
    'position',[10 60 200 200],...
    'string',str,...
    'HorizontalAlignment','left');