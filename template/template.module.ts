import { Module } from '@nestjs/common';

import { TEMPLATEController } from './template.controller';
import { TEMPLATERepository } from './template.repository';
import { TEMPLATEService } from './template.service';

import { CustomTypeOrmModule } from '~/common/typeorm/custom-typeorm.module';

@Module({
  imports: [CustomTypeOrmModule.forFeature([TEMPLATERepository], 'typeorm')],
  controllers: [TEMPLATEController],
  providers: [TEMPLATEService],
  exports: [TEMPLATEService, CustomTypeOrmModule],
})
export class TEMPLATEModule {}
