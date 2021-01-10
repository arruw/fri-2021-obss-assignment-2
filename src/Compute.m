basePath = 'data/physionet.org/files/tpehgdb/1.0.1/tpehgdb';

metadata = readtable('results/tpehgdb_metadata.csv');
metadata.Group = categorical(metadata.Group);
metadata.Premature = categorical(metadata.Premature);
metadata.Early = categorical(metadata.Early);

% skip first 180 seconds, sampling rate 20Hz
skip = 180*20;
channel = 12;

% sample entropy parameters
m = 3;
r = 0.15;

data = table(...
    'Size', [0 5],...
    'VariableNames', {'Record', 'Group', 'Rec_Time', 'Sample_Entropy', 'Median_Frequency'},...
    'VariableTypes', {'string', 'string', 'double', 'double', 'double'});

for i = 1:height(metadata)
    recordName = string(metadata{i,'Record'});
    recordTime = metadata{i,'Rec_Time'};
    recordGroup = string(metadata{i,'Group'});
    
    fprintf(sprintf('Processing record %s...\n', recordName));
    
    recordPath = sprintf('%s/%sm.mat', basePath, recordName);
    channels = load(recordPath).val(:,skip:end);
    
    sampleEntropy = sampen(channels(channel,:), m+1, r, 1, 0, 0);
    sampleEntropy = sampleEntropy(end);
    
    medianFreq = medfreq(channels(channel,:));
    
    data = [data; {
        recordName,...
        recordGroup,...
        recordTime,...
        sampleEntropy,...
        medianFreq
    }];
end

writetable(data, sprintf('results/sample_entropy_ch%d.csv', channel),...
    'Delimiter', ',',...
    'QuoteStrings', true);